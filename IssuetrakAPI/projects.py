from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class ProjectsMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing Projects
	"""
	@property
	def projects(self):
		if self._projects is None:
			self._projects = Projects(self, 'projects/')
		return self._projects


class Projects(GenericCaller):
	"""
	A Generic Caller class for Projects providing access by ID or as a complete set.
	"""
	def __init__(self, connector:APIConnector, endpoint_url:str):
		super().__init__(connector=connector, endpoint_url=endpoint_url)