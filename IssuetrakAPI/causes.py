from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class CausesMixIn(APIConnector):
	def causes(self):
		if self.causes is None:
			return self.causes = Causes(self, 'causes/')
		return self.causes


class Causes(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super(Causes, self).__init__(connector, endpoint_url)