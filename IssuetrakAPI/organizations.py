from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class OrganizationsMixIn(APIConnector):
	def organizations(self):
		if self.organizations is None:
			return self.organizations = Organizations(self, 'organizations/')
		return self.organizations


class Organizations(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super().__init__(connector, endpoint_url)
