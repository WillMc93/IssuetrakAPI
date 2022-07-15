from dataclasses import dataclass

@dataclass
class ReadIssueDTO:
	IssueNumber:int = -1
	IssueSolution:str = ''
	Status:str = ''
	ClosedBy:str = ''
	ClosedDate:str = ''
	SubmittedDate:str = ''
	CauseID:int = -1
	Subject:str = ''
	Description:str = ''
	IssueTypeID:int = -1
	IssueTypeID:int = -1
	IssueSubTypeID:int = -1
	IssueSubType2ID:int = -1
	IssueSubType3ID:int = -1
	IssueSubType4ID:int = -1
	Priority:str = ''
	AssetNumber:int = -1
	LocationID:str = ''
	SubmittedBy:str = ''
	AssignedTo:str = ''
	TargetDate:str = ''
	RequiredByDate:str = ''
	NextActionTo:str = ''
	SubStatusID:int = -1
	ProjectID:int = -1
	OrganizationID:int = -1
	ClassID:int = -1
	DepartmentID:int = -1
	SpecialFunction1:str = ''
	SpecialFunction2:str = ''
	SpecialFunction3:str = ''
	SpecialFunction4:str = ''
	SpecialFunction5:str = ''