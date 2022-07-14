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