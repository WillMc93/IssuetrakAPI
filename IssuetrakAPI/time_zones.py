from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class TimeZonesMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing Time Zones
	"""
	def time_zones(self):
		if self.time_zones is None:
			self.time_zones = Projects(self, 'timezones/')
		return self.time_zones


class TimeZones(GenericCaller):
	"""
	A Generic Caller class that provides access to Time Zones by ID or the full set
	"""