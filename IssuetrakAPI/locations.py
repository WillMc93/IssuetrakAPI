from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class LocationsMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing Locations
	"""
	@property
	def locations(self):
		if self._locations is None:
			self._locations = Locations(self, 'locations/')
		return self._locations


class Locations(GenericCaller):
	"""
	A Generic Caller class for Locations providing access by ID or as a complete set.
	"""
	def __init__(self,api_connector:APIConnector, endpoint_url:str):
		super().__init__(api_connector=api_connector, endpoint_url=endpoint_url)