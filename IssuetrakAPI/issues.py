from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class IssuesMixIn(APIConnector):
	def __init__(self, api_key, api_url):
		super(IssuesMixIn, self).__init__(api_key=api_key, api_url=api_url)
		self.issues = Issues(self, 'issues/')
		self.issue_types = IssueTypes(self, 'issuetypes/')
		self.issue_subtypes1 = IssuesSubTypes1(self, 'issuesubtypes1/')
		self.issue_subtypes2 = IssuesSubTypes2(self, 'issuesubtypes2/')
		self.issue_subtypes3 = IssuesSubTypes3(self, 'issuesubtypes3/')
		self.issue_subtypes4 = IssuesSubTypes4(self, 'issuesubtypes4/')

	def issues(self):
		if self.issues is None:
			self.issues = Issues(self, 'issues/')
		return self.issues

	def issue_types(self):
		if self.issue_types is None:
			self.issue_types = IssueTypes(self, 'issuetypes/')
		return self.issue_types

	def issue_subtypes1(self):
		if self.issue_subtypes1 is None:
			self.issue_subtypes1 = IssueSubTypes1(self, 'issuesubtypes1/')
		return self.issue_subtypes1

	def issue_subtypes2(self):
		if self.issue_subtypes2 is None:
			self.issue_subtypes2 = IssueSubTypes2(self, 'issuesubtypes2/')
		return self.issue_subtypes2

	def issue_subtypes3(self):
		if self.issue_subtypes3 is None:
			self.issue_subtypes3 = IssueSubTypes3(self, 'issuesubtypes3/')
		return self.issue_subtypes3

	def issue_subtypes4(self):
		if self.issue_subtypes4 is None:
			self.issue_subtypes4 = IssueSubTypes4(self, 'issuesubtypes4/')
		return self.issue_subtypes4


class IssueTypes(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super(IssueTypes, self).__init__(connector, endpoint_url)


class IssueSubTypes1(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super(IssueSubTypes1, self).__init__(connector, endpoint_url)


class IssueSubTypes2(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super(IssueSubTypes2, self).__init__(connector, endpoint_url)


class IssueSubTypes3(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super(IssueSubTypes3, self).__init__(connector, endpoint_url)


class IssueSubTypes4(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super(IssueSubTypes4, self).__init__(connector, endpoint_url)