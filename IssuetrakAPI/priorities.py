from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class PrioritiesMixIn(APIConnector):
	def priorities(self):
		if self.priorities is None:
			return self.priorities = Priorities(self, 'priorities/')
		return self.priorities


class Priorities(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super().__init__(connector, endpoint_url)
