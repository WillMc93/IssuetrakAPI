import base64
import hmac
import re
from datetime import datetime
from hashlib import sha512
from uuid import uuid4

import hyperlink
import requests

RE_CLEAN_HYPERLINK = re.compile(r'(?<!^https:)/{2,}')

class IssuetrakAPI:
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
		
		message = '\n'.join([http_verb, request_id, timestamp, absolute_path, request_query, request_body])
		hashed_message = self.__compute_hash(message)
		headers = {"X-IssueTrak-API-Request-ID": request_id,
			"X-IssueTrak-API-Timestamp": timestamp,
			"X-IssueTrak-API-Authorization": hashed_message,
			"content-type": "application/json"}

		return headers
	

	def __api_call(self, http_verb:str, endpoint_url:str, request_query:str='', request_body:str='') ->requests.Response:
		"""
		Generalized backend for requests to the API. 
		Makes sure the URL work is done and generates the headers before making the HTTP request.
		
		Will raise an exception if the http_verb has not been implemented.
		"""
		url = self.__sanitize_url(endpoint_url)
		headers = self.__generate_headers(url, http_verb, request_query, request_body)
		response = None		
		with self.session as sess:
			url_text = url.to_text()
			match http_verb:
				case 'GET':
					response = sess.get(url=url_text, headers=headers)
				case 'POST':
					response = sess.post(url=url_text, headers=headers, data=request_body)
				case 'PUT':
					response = sess.put(url=url_text, headers=headers, data=request_body)
				case _:
					raise Exception("The HTTP verb {http_verb} is unimplemented or invalid.")

		return response


	def perform_get(self, endpoint_url:str) -> requests.Response:
		"""
		Make a GET request
		"""
		return self.__api_call('GET', endpoint_url)


	def perform_post(self, endpoint_url:str, request_query:str='', request_body:str='') -> requests.Response:
		"""
		Make a POST request
		"""
		return self.__api_call('POST', endpoint_url, request_query, request_body)

	def perform_put(self, endpoint_url, request_query = '', request_body = '') -> requests.Response:
		"""
		Make a PUT request
		"""
		return self.__api_call('PUT', endpoint_url, request_query, request_body)