from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class LocationsMixIn(APIConnector):
	def locations(self):
		if self.locations is None:
			return self.locations = Locations(self, 'locations/')
		return self.locations


class Locations(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super(Locations, self).__init__(connector, endpoint_url)