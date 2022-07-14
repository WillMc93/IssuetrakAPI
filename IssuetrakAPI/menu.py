from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class MenuMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing Substatuses
	"""
	@property
	def menu(self):
		if self._menu is None:
			self._menu = Menu(self, 'menuitems/')
		return self._menu


class Menu(GenericCaller):
	"""
	A Generic Caller class for Menu Items providing access by ID or as a complete set.
	"""
	def __init__(self,api_connector:APIConnector, endpoint_url:str):
		super().__init__(api_connector=api_connector, endpoint_url=endpoint_url)