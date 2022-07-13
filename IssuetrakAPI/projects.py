from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class ProjectsMixIn(APIConnector):
	def projects(self):
		if self.projects is None:
			return self.projects = Projects(self, 'organizations/')
		return self.projects


class Projects(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super().__init__(connector, endpoint_url)
