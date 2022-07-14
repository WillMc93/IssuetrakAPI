class RequestException(Exception):
	"""
	Exception to be raised whenever a request encounters a problem.
	Displays the status code, and the verb/endpoint combo in question
	"""
	def __init__(self, http_verb:str, url:str, status_code:int):
		message = f'Request to API failed (status: {status_code}) with verb: '
				f'{http_verb} url: {url} combo.'
		super().__init__(message)
