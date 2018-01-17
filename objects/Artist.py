class Artist:
	def __init__(self, mbid, tmid, name, sortName, disambiguation, url):
		'''
			https://api.setlist.fm/docs/1.0/json_Artist.html
			parameters:
				- mbid - (String) unique MusicBrainz identifer
				- tmid - (Int) unique Ticket Master identifier
				- name - (String) the artist's name
				- sortName - (String) the artist's sort name
				- disambiguation - (String) disambiguation to distinguish between artist's with the same name
				- url - (String) the attribution url
		'''
		self.mbid = mbid
		self.tmid = tmid
		self.name = name
		self.sortName = sortName
		self.disambiguation = disambiguation
		self.url = url

	def getMbid():
		return self.mbid

