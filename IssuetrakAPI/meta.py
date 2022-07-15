from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import ConnectorCache

class MetaMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing Metadata
	"""
	@property_
	def metadata(self):
		if self._metadata is None:
			self._metadata = Metadata(self, 'metadata/')
		return self._metadata
		
class Metadata(ConnectorCache):
	"""
	A class providing http access to metadata. Issuetrak currently only supports 
	returning this info as a complete set, so this couldn't be a Generic Caller.
	"""
	def __init__(self, api_connector:APIConnector, endpoint_url:str):
		self.api_connector = api_connector
		self.endpoint_url = endpoint_url

	def get() -> dict:
		return = self.api_connector.perform_get(endpoint_url=self.endpoint_url)