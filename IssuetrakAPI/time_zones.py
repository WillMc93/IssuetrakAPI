from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class TimeZonesMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing Time Zones
	"""
	@property
	def time_zones(self):
		if self._time_zones is None:
			self._time_zones = Projects(self, 'timezones/')
		return self._time_zones


class TimeZones(GenericCaller):
	"""
	A Generic Caller class that provides access to Time Zones by ID or the full set
	"""