from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class MenuMixIn(APIConnector):
	def menu(self):
		if self.menu is None:
			return self.menu = menu(self, 'menuitems/')
		return self.menu


class Menu(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super(Menu, self).__init__(connector, endpoint_url)