class Country:
	def __init__(self, code, name):
		'''
			https://api.setlist.fm/docs/1.0/json_Country.html
			parameters:
				- code - (String) the country's ISO code
				- name - (String) the country's name
		'''
		self.code = code
		self.name = name