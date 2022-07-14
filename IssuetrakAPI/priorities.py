from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class PrioritiesMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing Substatuses
	"""
	@property
	def priorities(self):
		if self._priorities is None:
			self._priorities = Priorities(self, 'priorities/')
		return self._priorities


class Priorities(GenericCaller):
	"""
	A Generic Caller class for Priorities providing access by ID or as a complete set.
	"""