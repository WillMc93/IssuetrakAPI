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
	def __init__(self, connector, endpoint_url):
		self.connector = connector
		self.endpoint_url = endpoint_url

	def get() -> dict:
		return = self.connector.perform_get(endpoint_url=self.endpoint_url)