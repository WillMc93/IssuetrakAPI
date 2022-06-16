# Standard Library
import json
from urllib.parse import urljoin

# PyPI
import requests

SITE_URL = 'https://harbert.issuetrak.com/api/v2'
API_KEY_PATH = 'api2.key'

def read_api_key():
# Function for reading an API key from a UTF-8 file
	key = ''
	with open(API_KEY_PATH) as kf:
		key = kf.readline().strip()
	return key

class IssuetrakAPI:
	__api_key = ''
	__site_url = ''

	def __init__(self, api_key: str, site_url: str):
		self.__api_key = api_key
		self.__site_url = site_url

	def __generate_headers(self, request_type: str) -> dict:
		"""Generates and returns a dict containing the necessary request headers"""
		
		# Guard clause for request_type
		if request_type.upper() not in ['GET', 'POST', 'PUT', 'DELETE']:
			raise ValueError(f'request_type {request_type} is not a valid request type')

		# Initialize headers with necessary values
		headers = {}
		headers['accept'] = 'application/json'
		headers['X-Api-Key'] = self.api_key

		# Define optional values for POST and PUT requests
		if request_type.upper() == 'POST':
			headers['Content-Type'] = 'application/json'

		# TODO: Determine if we need additional header information for PUT and DELETEs

		return headers

	def perform_get(self, endpoint_url: str) -> requests.Response:
		"""Send GET request to issuetrack at the endpoint_url and
			return a request.Response object
		"""

		# Get headers for GET 
		headers = __generate_headers('GET')

		# Form full URL
		url = ''.join([self.__site_url, endpoint_url])

		# Do it
		return requests.get(url, headers=headers)