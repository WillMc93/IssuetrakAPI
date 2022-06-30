import base64
import hmac
import re
from datetime import datetime
from hashlib import sha512
from uuid import uuid4

import pdb

import hyperlink
import requests


RE_CLEAN_HYPERLINK = re.compile(r'(?<!^https:)/{2,}')


class IssuetrakAPI:
	def __init__(self, api_key: str, api_url: str):
		self.api_key = api_key
		self.api_url = api_url


	def __compute_hash(self, api_key:str, message:str) -> str:
		hash_text = None
		api_key_bytes = bytes(api_key, 'UTF-8')
		message_bytes = bytes(message, 'UTF-8')

		hmac_hash = hmac.new(api_key_bytes, message_bytes, sha512).digest()
		hash_text = base64.b64encode(hmac_hash).decode('UTF-8')
		
		return hash_text


	def __sanitize_url(self, endpoint_url: str) -> hyperlink.DecodedURL:
		"""
		Makes sure that the url is normalized and returns it as a hyperlink object
		"""
		full_url = '/'.join([self.api_url, endpoint_url])
		

		# Clean extraneous slashes
		full_url = RE_CLEAN_HYPERLINK.sub('/', full_url)

		# Get hyperlink and normalize
		url = hyperlink.parse(full_url)
		url = url.normalize()
		return url
	

	def __generate_headers(self, url:hyperlink.DecodedURL, http_verb='', request_query = '', request_body = ''):
		"""
		Generate the necessary headers for an api call
		"""
		request_id = str(uuid4()).lower()
		timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f0Z")
		url_path = '/'.join(url.path)
		
		message = '\n'.join([http_verb, request_id, timestamp, url_path, request_query, request_body])
		hashed_message = self.__compute_hash(self.api_key, message)
		
		headers = {"X-IssueTrak-API-Request-ID": request_id,
			"X-IssueTrak-API-Timestamp": timestamp,
			"X-IssueTrak-API-Authorization": hashed_message,
			"content-type": "application/json"}

		return headers


	def perform_get(self, endpoint_url):
		url = self.__sanitize_url(endpoint_url)
		headers = self.__generate_headers(url, 'GET')
		return requests.get(url.to_text(), headers)


	def perform_post(self, endpoint_url, request_query = '', request_body = ''):
		url = self.__sanitize_url(endpoint_url)
		headers = self.__generate_headers(url, 'POST', request_query, request_body)
		return requests.post(url.to_text(), headers)


	def perform_put(self, endpoint_url, request_query = '', request_body = ''):
		url = self.__sanitize_url(endpoint_url)
		headers = self.__generate_headers(url, 'PUT', request_query, request_body)
		return requests.put(url.to_text(), headers)