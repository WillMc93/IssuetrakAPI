from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class UserDefinedFieldTypesMixIn(APIConnector):
	def user_defined_field_types(self):
		if self.user_defined_field_types is None:
			return self.user_defined_field_types = UserDefinedFieldTypes(self, 'userdefinedfieldtypes/')
		return self.user_defined_field_types


class UserDefinedFieldTypes(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super().__init__(connector, endpoint_url)
