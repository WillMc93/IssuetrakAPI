from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class OrganizationsMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing Organizations
	"""
	@property
	def organizations(self):
		if self._organizations is None:
			self._organizations = Organizations(self, 'organizations/')
		return self._organizations


class Organizations(GenericCaller):
	"""
	A Generic Caller class for Organizations providing access by ID or as a complete set.
	"""