from IssuetrakAPI.api_connector import API_Connector


class CausesMixIn(API_Connector):
	def __init__(self, connector):
		self.connector = connector

	def causes(self):
		if self._causes is None:
			return self._causes = Causes()
		return self._causes




class CausesMixIn(API_Connector):
	