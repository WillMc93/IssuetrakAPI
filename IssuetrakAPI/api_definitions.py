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
		super().__init__(message)