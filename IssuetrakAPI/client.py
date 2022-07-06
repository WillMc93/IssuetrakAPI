from IssuetrakAPI.attachments import Attachements
from IssuetrakAPI.causes import Causes
from IssuetrakAPI.classes import Classes
from IssuetrakAPI.departments import Departments
from IssuetrakAPI.issues import Issues
from IssuetrakAPI.locations import Locations
from IssuetrakAPI.menu import Menu_Items
from IssuetrakAPI.meta import Metadata
from IssuetrakAPI.notes import Notes
from IssuetrakAPI.organizations import Organizations
from IssuetrakAPI.priorities import Priorities
from IssuetrakAPI.projects import Projects
from IssuetrakAPI.service import Service_Levels
from IssuetrakAPI.substatuses import Substatuses
from IssuetrakAPI.timezones import Timezones
from IssuetrakAPI.users import Users
from IssuetrakAPI.user_field_types import UserFieldTypes

class Client(Attachements, 
		Causes,
		Classes,
		Departments,
		Issues,
		Locations,
		Menu_Items,
		Metadata,
		Notes,
		Organizations,
		Priorities,
		Projects,
		Service_Levels,
		Substatuses,
		Timezones,
		Users,
		UserFieldTypes
		):

	def __init__(self, api_key:str='', api_url:str=''):
		super(Client, self).__init__(api_key=api_key, api_url=api_url)