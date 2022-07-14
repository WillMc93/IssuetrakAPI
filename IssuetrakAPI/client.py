from IssuetrakAPI.attachments import AttachementsMixIn
from IssuetrakAPI.causes import CausesMixIn
from IssuetrakAPI.classes import ClassesMixIn
from IssuetrakAPI.departments import DepartmentsMixIn
from IssuetrakAPI.issues import IssuesMixIn
from IssuetrakAPI.locations import LocationsMixIn
from IssuetrakAPI.menu import MenuMixIn
from IssuetrakAPI.meta import MetadataMixIn
from IssuetrakAPI.notes import NotesMixIn
from IssuetrakAPI.organizations import OrganizationsMixIn
from IssuetrakAPI.priorities import PrioritiesMixIn
from IssuetrakAPI.projects import ProjectsMixIn
from IssuetrakAPI.service import ServiceLevelsMixIn
from IssuetrakAPI.substatuses import SubstatusesMixIn
from IssuetrakAPI.timezones import TimezonesMixIn
from IssuetrakAPI.users import UsersMixIn
from IssuetrakAPI.user_field_types import UserFieldTypesMixIn

class Client(AttachementsMixIn, 
		CausesMixIn,
		ClassesMixIn,
		DepartmentsMixIn,
		IssuesMixIn,
		LocationsMixIn,
		MenuMixIn,
		MetadataMixIn,
		NotesMixIn,
		OrganizationsMixIn,
		PrioritiesMixIn,
		ProjectsMixIn,
		ServiceLevelsMixIn,
		SubstatusesMixIn,
		TimezonesMixIn,
		UsersMixIn,
		UserFieldTypesMixIn,
		):

	def __init__(self, api_key:str='', api_url:str=''):
		super(Client, self).__init__(api_key=api_key, api_url=api_url)