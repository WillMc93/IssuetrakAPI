#!/usr/bin/python3

import json

from csv import DictReader
from datetime import datetime

from IssuetrakAPI import IssuetrakAPI

"""
Constants
"""
# Path to the alert csv file
CSV_PATH = 'code42_alerts.csv'

# JSON ticket template
TICKET_TEMPLATE = {"ShouldNeverSendEmailForIssue": True,
					"SubmittedDate": str(datetime.now()),
					"EnteredBy": "COBTECH",
					"SubmittedBy": "COBTECH",
					"Subject": "TEST: Code42 Backup Sync Alert | {username}",
					"Description": "TEST: Code42 has not backed up in 7+ days for the following user</p> \
									<p>&nbsp;</p> \
									<table style=\"width: 100.0%; border-collapse: collapse;\" width=\"100%\"> \
									<tbody> \
									<tr> \
									<th>Username:</th> \
									<th>Computer Name:</th> \
									<th>Last Connection:</th> \
									<th>Last Backup:</th> \
									</tr> \
									<tr> \
									<td style=\"padding: 0in 37.5pt 0in 0in;\"> \
									<p style=\"text-align: center;\"><strong>{username}<br /></strong></p> \
									</td> \
									<td style=\"padding: 0in 37.5pt 0in 0in;\"> \
									<p style=\"text-align: center;\"><strong>{compname}</strong></p> \
									</td> \
									<td style=\"padding: 0in 37.5pt 0in 0in;\"> \
									<p style=\"text-align: center;\"><strong>{last_connect}<br /></strong></p> \
									</td> \
									<td style=\"padding: 0in 37.5pt 0in 0in;\"> \
									<p style=\"text-align: center;\"><strong>{last_backup}<br /></strong></p> \
									</td> \
									</tr> \
									</tbody> \
									</table> \
									<p>&nbsp;</p> \
									<p>Please investigate and make sure Code42 is active and properly backing up",
					"IsDescriptionRichText": True,
					"IssueTypeID": 3,
					"IssueSubTypeID": 130,
					"PriorityID": 4,
					"AssetNumber": 0,
					"LocationID": None,
					"AssignedTo": None,
					"TargetDate": None,
					"RequiredByDate": None,
					"NextActionTo": None,
					"SubStatusID": 6,
					"ProjectID": 0,
					"OrganizationID": 1,
					"ClassID": 1,
}


"""
Function definitions
"""
def extract_info(alert: dict) -> dict:
	# Extract needed info from the code42 alert entry
	extract = {}
	extract['username'] = alert['username']
	extract['compname'] = alert['deviceName']
	extract['last_connect'] = alert['lastConnectedDate']
	extract['last_backup'] = alert['lastCompletedBackupDate']

	return extract


def build_ticket(username: str, compname: str, last_connect: str, last_backup: str):
	# Fill out the code42 json dictonary
	ticket = TICKET_TEMPLATE.copy()
	ticket['Subject'] = ticket['Subject'].format(username=username)
	ticket['Description'] = ticket['Description'].format(username=username, compname=compname, \
														 last_connect=last_connect, last_backup=last_backup)

	return ticket


"""
Main
"""
if __name__ == '__main__':
	# Inititialize the API class
	api = IssuetrakAPI()

	# Read the code42 alerts and build the tickets
	tickets = []
	with open(CSV_PATH) as csvfile:
		code42 = DictReader(csvfile)
		for alert in code42:
			info = extract_info(alert)
			tickie = build_ticket(**info)
			tickets.append(tickie)

	# Submit the tickets via post
	for tickie in tickets:
		response = api.performPost("/issues", "", json.dumps(tickie))
		print(response.read().decode())
