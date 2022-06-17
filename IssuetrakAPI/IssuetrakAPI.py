# Standard Library
import json

# PyPI
import requests

class Issuetrak:

	def __init__(self, api_key: str, site_url: str):
		self.api_key = api_key
		self.site_url = site_url

	"""
	Define all backend functions
	"""
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

	def __perform_get(self, endpoint_url: str) -> requests.Response:
		"""Send GET request to issuetrack at the endpoint_url and
			return a request.Response object
		"""

		# Get headers for GET 
		headers = self.__generate_headers('GET')

		# Form full URL
		url = '/'.join([self.site_url, endpoint_url])

		# Do it
		return requests.get(url, headers=headers)

	def __perfrom_post(self, endpoint_url: str, request_body: dict) -> requests.Response:
		"""Send POST request to issuetrak at the endpoint_url and
			return a request.Response object.
		"""

		# Get headers for POST
		headers = self.__generate_headers('POST')

		# Form full URL
		url = '/'.join([self.site_url, endpoint_url])

		return requests.post(url, headers=headers, data=json.dumps(request_body))

	def __perform_put(self, endpoint_url: str, request_body: dict) -> requests.Response:
		"""Send PUT request to issuetrak at the endpoint_url and 
			return a request.Response object
		"""

		# Get headers for PUT
		headers = self.__generate_headers('PUT')

		# Form full URL
		url = '/'.join([self.site_url, endpoint_url])

		return requests.put(url, headers=headers, data=json.dumps(request_body))

	def __perform_delete(self, endpoint_url: str, request_body: dict) -> requests.Response:
		"""Send DELETE request to Issuetrak at the endpoint_url and 
			return a request.Response object
		"""

		# Get headers for DELETE
		headers = self.__generate_headers('DELETE')

		# Form full URL
		url = '/'.join([self.site_url, endpoint_url])

		return requests.delete(url, headers=headers, data=json.dumps(request_body))

	def __gather_all(self, call: )

	"""
	Define all GET requests

	All return a tuple of the traceID string and the data as a dict indexed by iid
	"""
	def get_departments(self) -> dict:
		"""Get all departments"""

		pass

	def get_all_groups(self) -> dict:
		"""Get all groups"""
		pass

	def get_group(self, group_iid: str) -> dict:
		"""Get a group by IID"""
		pass

	def get_group_organizations(self, group_iid: str) -> dict:
		"""Get a groups organization memeberships"""
		pass

	def get_all_locations(self) -> dict:
		"""Get all locations"""
		pass

	def get_all_organizations(self) -> dict:
		"""Get all organizations"""
		pass

	def get_organization(self, organization_iid: str) -> dict:
		"""Get an organization by IID"""
		pass

	def get_organizations_udfs(self) -> dict:
		"""Get user defined field definitions for organizations"""
		pass

	def get_system(self) -> dict:
		"""Get Issuetrak settings"""
		pass

	def get_users(self) -> dict:
		"""Get all users"""
		pass

	def get_users_by_iid(self, user_iid: str) -> dict:
		"""Get a user by iid"""
		pass

	def get_users_udfs(self) -> dict:
		"""Get user defined field definitions for users"""
		pass

	def get_users_groups(self, user_iid: str) -> dict:
		"""Get user's group memberships"""
		pass

	def get_users_organizations(self, user_iid: str) -> dict:
		"""Get user's organization memeberships"""
		pass
