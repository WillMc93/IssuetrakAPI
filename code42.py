
from csv import DictReader
from datetime import datetime

from IssuetrakAPI import IssuetrakAPI

CSV_PATH = 'code42.csv'

# Inititialize the API class
api = IssuetrakAPI()

# Read the Code42 csv into a dictionary
code42 = DictReader(CSV_PATH)


#######################################
# POST
# Insert issue into Issuetrak
#######################################

# Set disabled/inactive fields to None
requestBody = {
  "ShouldSuppressEmailForCreateOperation": True,
  "Notes": [
    {
      "CreatedDate": f"{datetime.now()}",
      "CreatedBy": "Code42 Script",
      "NoteText": "This is a note",
      "IsPrivate": False,
      "IsRichText": True
    }
  ],
  "UserDefinedFields": [
    {
      "UserDefinedFieldID": 1,
      "Value": "This is text that will go into one of my user defined fields"
    },
    {
      "UserDefinedFieldID": 1008,
      "Value": f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}"
    }
  ],
  "SubmittedDate": f"{datetime.now()}",
  "EnteredBy": "admin",
  "SeverityID": None,
  "Subject": "This is a test subject submitted via the Issuetrak API in Python",
  "Description": "This is the description of the test issue",
  "IsDescriptionRichText": True,
  "IssueTypeID": 1,
  "IssueSubTypeID": 0,
  "IssueSubType2ID": 0,
  "IssueSubType3ID": 0,
  "IssueSubType4ID": None,
  "PriorityID": 1,
  "AssetNumber": 0,
  "LocationID": "",
  "SubmittedBy": "admin",
  "AssignedTo": None,
  "TargetDate": None,
  "RequiredByDate": None,
  "NextActionTo": None,
  "SubStatusID": 0,
  "ProjectID": 0,
  "OrganizationID": 1,
  "ShouldNeverSendEmailForIssue": False,
  "ClassID": 1,
  "DepartmentID": None,
  "SpecialFunction1": "string",
  "SpecialFunction2": "string",
  "SpecialFunction3": "string",
  "SpecialFunction4": "string",
  "SpecialFunction5": "string"
}

print("\n\n------Insert Issue------")
#response = apiAuthorization.performPost("/issues", "", json.dumps(requestBody))
print(response.read().decode())