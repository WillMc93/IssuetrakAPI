from uuid import uuid4
from urllib.parse import urlparse
from hashlib import sha512
from datetime import datetime
import hmac
import json
import base64
import http.client

import requests


class IssuetrakAPI:
	def __init__(self, api_key, api_url):
		self.api_key = api_key
		self.api_url = api_url

	def __compute_hash(self, api_key, message):
		hash_text = None
		api_key_bytes = bytes(api_key, 'UTF-8')
		message_bytes = bytes(message, 'UTF-8')

		hmac_hash = hmac.new(api_key_bytes, message_bytes, sha512).digest()
		hash_text = base64.b64encode(hmac_hash).decode('UTF-8')
		
		return hash_text

	def __generate_headers(self, request_id, timestamp, hashed_message):
		headers = {"X-IssueTrak-API-Request-ID": request_id,
			"X-IssueTrak-API-Timestamp": timestamp,
			"X-IssueTrak-API-Authorization": hashed_message,
			"content-type": "application/json"}

		return headers

	def __performApiCall(self, http_verb, endpoint_url, request_query = "", request_body = ""):
		full_url = f"{self.siteUrl}{endpoint_url}"
		url_parts = urlparse(full_url)
		base_url = url_parts.netloc.lower()
		absolutePath = urlparse(full_url).path.lower()
		requestId = str(uuid4()).lower()
		timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f0Z")
		message = '\n'.join([http_verb, request_id, time_stamp, absoluteUrlPath, requestQuery, requestBody])
		hashedMessage = self.__compute_hash(self.__apiKey, messageToHash)
		
		connection = self.__getConnection(urlParts.scheme, baseUrl)
		headers = self.__generateHeaders(requestId, requestTimestamp, hashedMessage)

		connection.request(httpVerb, fullUrl, requestBody, headers)
		return connection.getresponse()

	def performGet(self, endpointUrl):
		return self.__performApiCall("GET", endpoint_url)

	def performPost(self, endpointUrl, requestQuery = '', requestBody = ''):
		return self.__performApiCall("POST", endpoint_url, requestQuery, requestBody)

	def performPut(self, endpointUrl, requestQuery = '', requestBody = ''):
		return self.__performApiCall("PUT", endpoint_url, requestQuery, requestBody)

