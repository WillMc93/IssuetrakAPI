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
TICKET_TEMPLATE = {
	"ShouldNeverSendEmailForIssue": True,
	
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

	# TODO: Fillout ticket

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
			tickie = build_ticket(*info)
			tickets.append(tickie)

	# Submit the tickets via post
	for tickie in tickets:
		response = apiAuthorization.performPost("/issues", "", json.dumps(requestBody))



	

#######################################
# POST
# Insert issue into Issuetrak
#######################################

response = api.performGet('/issues/false/18875')
response_data = response.read().decode()
json_decoder = json.JSONDecoder()
decoded = json_decoder.decode(response_data)

print(response.read().decode())