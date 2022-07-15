from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class IssuesMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespace for accessing Issues, Issue Types, and Issue Subtypes
	"""
	@property
	def issues(self):
		if self._issues is None:
			self._issues = Issues(self, 'issues/')
		return self._issues

	@property
	def issue_types(self):
		if self._issue_types is None:
			self._issue_types = IssueTypes(self, 'issuetypes/')
		return self._issue_types

	@property
	def issue_subtypes1(self):
		if self._issue_subtypes1 is None:
			self._issue_subtypes1 = IssueSubTypes1(self, 'issuesubtypes1/')
		return self._issue_subtypes1

	@property
	def issue_subtypes2(self):
		if self._issue_subtypes2 is None:
			self._issue_subtypes2 = IssueSubTypes2(self, 'issuesubtypes2/')
		return self._issue_subtypes2

	@property
	def issue_subtypes3(self):
		if self._issue_subtypes3 is None:
			self._issue_subtypes3 = IssueSubTypes3(self, 'issuesubtypes3/')
		return self._issue_subtypes3

	@property
	def issue_subtypes4(self):
		if self._issue_subtypes4 is None:
			self._issue_subtypes4 = IssueSubTypes4(self, 'issuesubtypes4/')
		return self._issue_subtypes4


class Issues(ConnectorCache):
	"""
	A class providing access to issues. 
	"""
	def __init__(self,api_connector:APIConnector, endpoint_url:str)
		super().__init__(api_connector=api_connector)
		self.endpoint_url = endpoint_url

	def get_by_id(issue_numbers:int|list(int), include_notes=False):
		if type(issue_number) is int:
			endpoint_url = f'{self.endpoint_url}/{include_notes}/{issue_numbers}'
		elif type(issue_number) is list:
			issue_str = ','.join(issue_numbers)
			endpoint_url = f'{self.endpoint_url}/{include_notes}/?issueNumbers={issue_str}'
		return self.api_connector.perform_get(endpoint_url)



class IssueTypes(GenericCaller):
	"""
	A Generic Caller class for Issue Types providing access by ID or as a complete set.
	"""
	def __init__(self,api_connector:APIConnector, endpoint_url:str):
		super().__init__(api_connector=api_connector, endpoint_url=endpoint_url)


class IssueSubTypes1(GenericCaller):
	"""
	A Generic Caller class for Issue Subtypes 1 providing access by ID or as a complete set.
	"""
	def __init__(self,api_connector:APIConnector, endpoint_url:str):
		super().__init__(api_connector=api_connector, endpoint_url=endpoint_url)


class IssueSubTypes2(GenericCaller):
	"""
	A Generic Caller class for Issue Subtypes 2 providing access by ID or as a complete set.
	"""
	def __init__(self,api_connector:APIConnector, endpoint_url:str):
		super().__init__(api_connector=api_connector, endpoint_url=endpoint_url)


class IssueSubTypes3(GenericCaller):
	"""
	A Generic Caller class for Issue Subtypes 3 providing access by ID or as a complete set.
	"""
	def __init__(self,api_connector:APIConnector, endpoint_url:str):
		super().__init__(api_connector=api_connector, endpoint_url=endpoint_url)


class IssueSubTypes4(GenericCaller):
	"""
	A Generic Caller class for Issue Subtypes 4 providing access by ID or as a complete set.
	"""
	def __init__(self,api_connector:APIConnector, endpoint_url:str):
		super().__init__(api_connector=api_connector, endpoint_url=endpoint_url)