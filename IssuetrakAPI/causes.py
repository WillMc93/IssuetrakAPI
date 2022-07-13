from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class CausesMixIn(APIConnector):

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