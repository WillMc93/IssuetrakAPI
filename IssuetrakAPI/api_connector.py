import base64
import hmac
import re
from datetime import datetime
from hashlib import sha512
from uuid import uuid4

import hyperlink
import requests

from api_exceptions import RequestException

RE_CLEAN_HYPERLINK = re.compile(r'(?<!^https:)/{2,}')

class APIConnector:
	def __init__(self, api_key: str, api_url: str):
		"""
		Constructor records the api key, the host url, and starts a requests session
		"""
		self.api_key = api_key
		self.api_url = api_url
		self.session = requests.Session()


	def __compute_hash(self, message:str) -> str:
		"""
		Computes a SHA512 HMAC of the HTTP request
		"""
		api_key_bytes = bytes(self.api_key, 'UTF-8')
		message_bytes = bytes(message, 'UTF-8')

		hmac_hash = hmac.new(api_key_bytes, message_bytes, sha512).digest()
		hash_text = base64.b64encode(hmac_hash).decode('UTF-8')
		return hash_text


	def __sanitize_url(self, endpoint_url:str) -> hyperlink.DecodedURL:
		"""
		Makes sure that the url is constructed correctly and normalized, and 
		returns a hyperlink URL-object
		"""
		# Construct
		full_url = '/'.join([self.api_url, endpoint_url])
		
		# Clean extraneous slashes
		full_url = RE_CLEAN_HYPERLINK.sub('/', full_url)

		# Make hyperlink object and normalize
		url = hyperlink.parse(full_url)
		url = url.normalize()
		return url
	

	def __generate_headers(self, full_url:hyperlink.DecodedURL, http_verb:str='', request_query:str='', request_body:str='') -> dict:
		"""
		Generate the necessary HTTP headers for the API call
		"""
		request_id = str(uuid4()).lower()
		timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f0Z")
		absolute_path = '/'.join(url.path)
		absolute_path = '/' + absolute_path.lower()
		
		message = [http_verb, request_id, timestamp, absolute_path, request_query, request_body]
		message = '\n'.join(message)
		hashed_message = self.__compute_hash(message)
		headers = {"X-IssueTrak-API-Request-ID": request_id,
			"X-IssueTrak-API-Timestamp": timestamp,
			"X-IssueTrak-API-Authorization": hashed_message,
			"content-type": "application/json"}

		return headers
	

	def __api_call(self, http_verb:str, endpoint_url:str, request_query:str='', request_body:str='') -> dict:
		"""
		Generalized backend for requests to the API. 
		Makes sure the URL work is done and generates the headers before making the HTTP request.
		
		Will raise an exception if the http_verb has not been implemented.
		Will raise a RequestException (api_definitions.py) if the request does not return a 200 status.
		"""
		url = self.__sanitize_url(endpoint_url)
		url_text = url.to_text()
		headers = self.__generate_headers(url, http_verb, request_query, request_body)
		response = None		
		with self.session as sess:
			url_text = url.to_text()
			if http_verb == 'GET':
				response = sess.get(url=url_text, headers=headers).content
			elif http_verb == 'POST':
				response = sess.post(url=url_text, headers=headers, data=request_body)
			elif http_verb == 'PUT':
				response = sess.put(url=url_text, headers=headers, data=request_body)
			else:
				raise Exception("The HTTP verb {http_verb} is unimplemented or invalid.")

		if r.status_code == 200:
			response = response.json()
		else:
			raise RequestException(http_verb=http_verb, url=url_text, status=response.status_code)

		return response


	def perform_get(self, endpoint_url:str) -> dict:
		"""
		Make a GET request
		"""
		return self.__api_call('GET', endpoint_url)


	def perform_post(self, endpoint_url:str, request_query:str='', request_body:str='') -> dict:
		"""
		Make a POST request
		"""
		return self.__api_call('POST', endpoint_url, request_query, request_body)

	def perform_put(self, endpoint_url:str, request_query:str='', request_body:str='') -> dict:
		"""
		Make a PUT request
		"""
		return self.__api_call('PUT', endpoint_url, request_query, request_body)