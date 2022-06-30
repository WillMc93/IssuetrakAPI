import os
import re
import pdb

LABELS = ['apiv1', 'apiv2']
RE_KEY_DELIMITER = re.compile(r':\s*')

def read_api_key(path: str) -> dict:
	"""
	Read each labeled API key in the designated path and return them as a list.

	TODO: If/when API v2 is finalized correct this to only look for one API key
	"""
	# Guard clause to check that path is valid
	if not os.path.isfile(path):
		raise ValueError(f"The API key file path {path} does not appear to exist.")

	# Load the keys from file
	keys = {label: None for label in LABELS}
	with open(path) as kf:
		data = kf.readlines()
		for keypair in data:
			keypair = keypair.strip()
			label, key = RE_KEY_DELIMITER.split(keypair, maxsplit=1)
			if label in LABELS:
				keys[label] = key

	# Check validity of loaded keys
	# keys need to have a trailing =
	for key in keys:
		if keys[key][-1] != '=':
			raise ValueError(f"The API key {key} doesn't appear to be a correctly formatted API key (no '=' at end).")
	return keys

# For testing only
if __name__ == '__main__':
	path = 'api.key'

	print(read_api_key(path))