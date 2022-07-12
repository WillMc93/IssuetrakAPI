from IssuetrakAPI.api_connector import API_Connector
from IssuetrakAPI.api_definitions import Connector_Cache


class CausesMixIn(API_Connector):
	def __init__(self, connector):
		self.connector = connector

	def causes(self):
		if self._causes is None:
			return self._causes = Causes(self.connector)
		return self._causes


class Causes(Connector_Cache):
	def __clean_dict(json_data:dict) -> dict:


	def get_by_id(cause_id:int) -> dict:
		endpoint_url = f'causes/{cause_id}'
		json_data = self.connector.perform_post(endpoint_url=endpoint_url)
		data = __clean_dict(json_data)
		return data

	def get_all() -> dict:
		endpoint_url = 'causes'
		json_data = self.connector.perform_get(endpoint_url=endpoint_url)
		data = __clean_dict(json_data)
		return data




