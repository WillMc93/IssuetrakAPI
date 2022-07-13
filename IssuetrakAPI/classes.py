from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class ClassesMixIn(APIConnector):
	def classes(self):
		if self.classes is None:
			return self.classes = Classes(self, 'classes/')
		return self.classes


class Classes(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super().__init__(connector, endpoint_url)
