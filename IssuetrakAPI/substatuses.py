from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class SubstatusesMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing Substatuses
	"""
	@property
	def substatuses(self):
		if self._substatuses is None:
			self._substatuses = Substatuses(self, 'substatuses/')
		return self._substatuses


class Substatuses(GenericCaller):
	"""
	A Generic Caller class for Substatuses providing access by ID or as a complete set.
	"""
	def __init__(self,api_connector:APIConnector, endpoint_url:str):
		super().__init__(api_connector=api_connector, endpoint_url=endpoint_url)