# Standard Library
import json

# PyPI
import requests

SITE_URL = 'https://harbert.issuetrak.com/api/v2'
API_KEY_PATH = 'api2.key'

def read_api_key(key_path=API_KEY_PATH: str) -> str:
	"""Function for reading an API key from a UTF-8 file"""
	key = ''
	with open(API_KEY_PATH) as kf:
		key = kf.readline().strip()
	return key

class IssuetrakAPI:

	def __init__(self, api_key='': str, site_url=SITE_URL: str):
		if api_key = ''
			api_key = read_api_key()
		self.api_key = api_key
		self.site_url = site_url

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
		url = '/'.join([self.site_url, endpoint_url])

		# Do it
		return requests.get(url, headers=headers)

	def perfrom_post(self, endpoint_url: str, request_body: dict) -> requests.Response:
		"""Send POST request to issuetrak at the endpoint_url and
			return a request.Response object.
		"""

		# Get headers for POST
		headers = __generate_headers('POST')

		# Form full URL
		url = '/'.join([self.site_url, endpoint_url])

		return requests.post(url, headers=headers, data=json.dumps(request_body))

	def perform_put(self, endpoint_url: str, request_body: dict) -> requests.Response:
		"""Send PUT request to issuetrak at the endpoint_url and 
			return a request.Response object
		"""

		# Get headers for PUT
		headers = __generate_headers('PUT')

		# Form full URL
		url = '/'.join([self.site_url, endpoint_url])

		return requests.put(url, headers=headers, data=json.dumps(request_body))
