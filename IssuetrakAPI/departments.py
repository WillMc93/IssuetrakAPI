from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class DepartmentsMixIn(APIConnector):
	def departments(self):
		if self.departments is None:
			return self.departments = Departments(self, 'departments/')
		return self.departments


class Departments(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super(Departments, self).__init__(connector, endpoint_url)