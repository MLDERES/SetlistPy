class Venue:
	def __init__(self, city, url, venueId, name):
		'''
			https://api.setlist.fm/docs/1.0/json_Venue.html
			parameters:
				- city - (City) the city in which the venue is located
				- url - (String) the attribution url
				- venueId - (String) unique identifier
				- name - (String) the name of the venue, usually without city and country
		'''
		self.city = city
		self.url = url
		self.venueId = venueId
		self.name = name