from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class ServiceLevelMixIn(APIConnector):
	def service_levels(self):
		if self.service_levels is None:
			return self.service_levels = ServiceLevels(self, 'servicelevels/')

	def service_level_agreements(self):
		if self.service_level_agreements is None:
			return self.service_level_agreements = ServiceLevelAgreements(self, 'servicelevelagreements/')
		return self.service_level_agreements

	def service_level_severities(self):
		if self.service_level_severities is None:
			return self.service_level_severities = ServiceLevelSeverities(self, 'servicelevelseverities/')
		return self.service_level_severities

	def service_level_terms(self):
		if self.service_level_terms is None:
			return self.service_level_terms = ServiceLevelTerms(self, 'servicelevelterms/')
		return self.service_level_terms


class ServiceLevels(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super().__init__(connector, endpoint_url)


class ServiceLevelAgreements(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super().__init__(connector, endpoint_url)


class ServiceLevelSeverities(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super().__init__(connector, endpoint_url)


class ServiceLevelTerms(GenericCaller):
	def __init__(self, connector, endpoint_url):
		super().__init__(connector, endpoint_url)

