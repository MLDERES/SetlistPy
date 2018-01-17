class Coords:
	def __init__(self, coordsLong, coordsLat):
		'''
			https://api.setlist.fm/docs/1.0/json_Coords.html
			parameters:
				- coordsLong - (Int) the longitude part of the coordinates
				- coordsLat - (Int) the latitude part of the coordinates
		'''
		self.long = coordsLong
		self.lat = coordsLat