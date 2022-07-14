from api_connector import APIConnector

class ConnectorCache:
	"""
	Caches an API Connctor. 
	Standardizes the initialization of any class that access the API Connector.
	"""
	def __init__(self, api_connector:APIConnector):
		self.connector = api_connector


class RequestException(Exception):
	"""
	Exception to be raised whenever a request encounters a problem.
	Displays the status code, and the verb/endpoint combo in question
	"""
	def __init__(self, http_verb:str, url:str, status_code:int):
		message = f'Request to API failed (status: {status_code}) with verb: '
				f'{http_verb} url: {url} combo.'
		super().__init__(message)


class GenericCaller(ConnectorCache):
	"""
	A class for all requestors that just need to provide returning by id, 
	and returning all with no server-side filtering/decoding.

	Classes of this type include:
		* Causes
		* Classes
		* Departments
		* Locations
		* Menu
		* Organizations
		* Priorities
		* ServiceLevels (Agreements, Severities, and Terms)
		* Substatuses
		* TimeZones
		* UserDefinedFieldTypes
	"""
	def __init__(self, connector:APIConnector, endpoint_url:str):
		super(GenericCaller, self).__init__(connector)
		self.endpoint_url = endpoint_url
		
	def get_by_id(_id:int) -> dict:
		endpoint_url = f'{self.endpoint_url}/{_id}'
		return self.connector.perform_post(endpoint_url=self.endpoint_url)

	def get_all() -> dict:
		return = self.connector.perform_get(endpoint_url=self.endpoint_url)