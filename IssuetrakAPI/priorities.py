from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class PrioritiesMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing Substatuses
	"""
	@property
	def priorities(self):
		if self._priorities is None:
			self._priorities = Priorities(self, 'priorities/')
		return self._priorities


class Priorities(GenericCaller):
	"""
	A Generic Caller class for Priorities providing access by ID or as a complete set.
	"""
	def __init__(self,api_connector:APIConnector, endpoint_url:str):
		super().__init__(api_connector=api_connector, endpoint_url=endpoint_url)