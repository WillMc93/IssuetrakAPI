from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class UserDefinedFieldTypesMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing User Defined Field Types
	"""
	@property
	def user_defined_field_types(self):
		if self._user_defined_field_types is None:
			self._user_defined_field_types = UserDefinedFieldTypes(self, 'userdefinedfieldtypes/')
		return self._user_defined_field_types


class UserDefinedFieldTypes(GenericCaller):
	"""
	A Generic Caller class that provides getting by ID and getting all for
	User Defined Field Types
	"""
