from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class DepartmentsMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing Departments
	"""
	@property
	def departments(self):
		if self._departments is None:
			self._departments = Departments(self, 'departments/')
		return self._departments


class Departments(GenericCaller):
	"""
	A Generic Caller class for Departments providing access by ID or as a complete set.
	"""
	def __init__(self, connector:APIConnector, endpoint_url:str):
		super().__init__(connector=connector, endpoint_url=endpoint_url)