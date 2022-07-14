from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class CausesMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing Causes
	"""
	@property
	def causes(self):
		if self._causes is None:
			self._causes = Causes(self, 'causes/')
		return self._causes


class Causes(GenericCaller):
	"""
	A Generic Caller class for Causes providing access by ID or as a complete set.
	"""