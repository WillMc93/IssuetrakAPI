from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class TimeZonesMixIn(APIConnector):
	def time_zones(self):
		if self.time_zones is None:
			return self.time_zones = Projects(self, 'timezones/')
		return self.time_zones


class TimeZones(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super().__init__(connector, endpoint_url)
