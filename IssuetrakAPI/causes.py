from IssuetrakAPI.api_connector import API_Connector
from IssuetrakAPI.api_definitions import Connector_Cache


class CausesMixIn(API_Connector):
	def __init__(self, connector):
		self.connector = connector
		self.causes = None

	def causes(self):
		if self.causes is None:
			return self.causes = Causes(self.connector)
		return self.causes


class Causes(Connector_Cache):
	def get_by_id(cause_id:int) -> dict:
		endpoint_url = f'causes/{cause_id}'
		return self.connector.perform_post(endpoint_url=endpoint_url)

	def get_all() -> dict:
		endpoint_url = 'causes'
		return = self.connector.perform_get(endpoint_url=endpoint_url)