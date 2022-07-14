from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import ConnectorCache

class MetaMixIn(APIConnector):
	def metadata(self):
		if self.metadata is None:
			return self.metadata = Metadata(self, 'metadata/')
		return self.metadata
		
class Metadata(ConnectorCache):
	def __init__(self, connector, endpoint_url):
		self.connector = connector
		self.endpoint_url = endpoint_url

	def get() -> dict:
		return = self.connector.perform_get(endpoint_url=self.endpoint_url)