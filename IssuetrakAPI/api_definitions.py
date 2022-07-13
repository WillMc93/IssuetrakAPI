from api_connector import API_Connector

class Connector_Cache:
	"""
	Caches an API Connctor. 
	Standardizes the initialization of any class that access the API Connector.
	"""
	def __init__(self, api_connector:API_Connector):
		self.connector = api_connector

class RequestException(Exception):
	def __init__(self, http_verb:str, url:str):
		message = f'Request to API failed with verb: {http_verb} url: {url} combo.'
		super().__init__(message)class GenericCaller(ConnectorCache):
	"""
	A class for all requestors that just need a get by id, and a get all with
	no server-side filtering/decoding.

	Classes of this type include:
		* Causes
		* Classes
		* Departments
		* Locations
		* Menu
		* Organizations
	"""
	def __init__(self, connector:APIConnector, endpoint_url:str):
		super(GenericCaller, self).__init__(connector)
		self.endpoint_url = endpoint_url
		
	def get_by_id(_id:int) -> dict:
		endpoint_url = f'{self.endpoint_url}/{_id}'
		return self.connector.perform_post(endpoint_url=self.endpoint_url)

	def get_all() -> dict:
		return = self.connector.perform_get(endpoint_url=self.endpoint_url)