from IssuetrakAPI.api_connector import APIConnector
from IssuetrakAPI.api_definitions import GenericCaller


class ServiceLevelMixIn(APIConnector):
	"""
	Mix-in class providing convenient namespaces for accessing Service Level information
	"""
	@property
	def service_levels(self):
		if self._service_levels is None:
			self._service_levels = ServiceLevels(self, 'servicelevels/')
		return self._service_levels

	@property
	def service_level_agreements(self):
		if self._service_level_agreements is None:
			self._service_level_agreements = ServiceLevelAgreements(self, 'servicelevelagreements/')
		return self._service_level_agreements

	@property
	def service_level_severities(self):
		if self._service_level_severities is None:
			self._service_level_severities = ServiceLevelSeverities(self, 'servicelevelseverities/')
		return self._service_level_severities

	@property
	def service_level_terms(self):
		if self._service_level_terms is None:
			self._service_level_terms = ServiceLevelTerms(self, 'servicelevelterms/')
		return self._service_level_terms


class ServiceLevels(GenericCaller):
	"""
	A Generic Caller class for Service Levels providing access by ID or as a complete set.
	"""
	def __init__(self, connector:APIConnector, endpoint_url:str):
		super().__init__(connector=connector, endpoint_url=endpoint_url)


class ServiceLevelAgreements(GenericCaller):
	"""
	A Generic Caller class for Service Levels Agreements providing access by ID or as a complete set.
	"""
	def __init__(self, connector:APIConnector, endpoint_url:str):
		super().__init__(connector=connector, endpoint_url=endpoint_url)


class ServiceLevelSeverities(GenericCaller):
	"""
	A Generic Caller class for Service Levels Severities providing access by ID or as a complete set.
	"""
	def __init__(self, connector:APIConnector, endpoint_url:str):
		super().__init__(connector=connector, endpoint_url=endpoint_url)


class ServiceLevelTerms(GenericCaller):
	"""
	A Generic Caller class for Service Levels Terms providing access by ID or as a complete set.
	"""
	def __init__(self, connector:APIConnector, endpoint_url:str):
		super().__init__(connector=connector, endpoint_url=endpoint_url)