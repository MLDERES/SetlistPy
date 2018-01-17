class Error:
	def __init__(self, code, status, message, timestamp):
		'''
			https://api.setlist.fm/docs/1.0/json_Error.html
			parameters:
				- code - (Int) the HTTP status code
				- status - (String) the HTTP status message
				- message - (String) an additional error message
				- timestamp - (String) current timestamp
		'''
		self.code = code
		self.status = status
		self.message = message
		self.timestamp = timestamp