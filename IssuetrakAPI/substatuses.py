from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class SubstatusesMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing Substatuses
	"""
	def substatuses(self):
		if self.substatuses is None:
			self.substatuses = Substatuses(self, 'substatuses/')
		return self.substatuses


class Substatuses(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super().__init__(connector, endpoint_url)
