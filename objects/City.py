class City:
	def __init__(self, cityId, name, stateCode, state, coords, country):
		'''
			https://api.setlist.fm/docs/1.0/json_City.html
			params:
				- cityId - (String) unique identifier
				- name - (String) the city's name
				- stateCode - (String) the code of the city's state
				- state - (String) the name of city's state
				- coords - (Coords) the city's coordinates
				- country - (Country) the city's country
		'''
		self.cityId = cityId
		self.name = name
		self.stateCode = stateCode
		self.state = state
		self.coords = coords
		self.country = country