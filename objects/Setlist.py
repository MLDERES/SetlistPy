class Setlist:
	def __init__(self, artist, venue, tour, sets, info, url, setlistId, versionId, eventDate, lastUpdated):
		'''
			https://api.setlist.fm/docs/1.0/json_Setlist.html
			parameters:
				- artist - (Artist) the setlist's artist
				- venue - (Venue) the setlist's venue
				- tour - (Tour) the setlist's tour
				- sets - (array of Set) all sets of this setlist
				- info - (String) additional information on the concert
				- url - (String) the attribution url to which you have to link to wherever you use data from this setlist in your application
				- setlistId - (String) unique identifier
				- versionId - (String) unique identifier of the version
				- eventDate - (String) date of the concert in the form "dd-MM-yyyy"
				- lastUpdated - (String) date, time, and time zone of the last update to this setlist in the format "yyyy-MM-dd'T'HH:mm:ss.SSSZZZZZ"
		'''
		self.artist = artist
		self.venue = venue
		self.tour = tour
		self.set = [x for x in sets]
		self.info = info
		self.url = url
		self.setlistId = setlistId
		self.versionId = versionId
		self.eventDate = eventDate
		self.lastUpdated = lastUpdated