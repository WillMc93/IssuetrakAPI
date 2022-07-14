from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class ClassesMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing Classes
	"""
	@property
	def classes(self):
		if self._classes is None:
			self._classes = Classes(self, 'classes/')
		return self._classes


class Classes(GenericCaller):
	"""
	A Generic Caller class for Classes providing access by ID or as a complete set.
	"""
	def __init__(self,api_connector:APIConnector, endpoint_url:str):
		super().__init__(api_connector=api_connector, endpoint_url=endpoint_url)