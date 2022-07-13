from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import ConnectorCache

class Meta(ConnectorCache):
	def __init__(self, connector:APIConnector, endpoint_url:str):
		super(Meta, self).__init__(connector)
		self.endpoint_url = endpoint_url
		
	def get_all() -> dict:
		return = self.connector.perform_get(endpoint_url=self.endpoint_url)