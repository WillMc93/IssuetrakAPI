from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class SubstatusesMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing Substatuses
	"""
	@property
	def substatuses(self):
		if self._substatuses is None:
			self._substatuses = Substatuses(self, 'substatuses/')
		return self._substatuses


class Substatuses(GenericCaller):
	"""
	A Generic Caller class for Substatuses providing access by ID or as a complete set.
	"""