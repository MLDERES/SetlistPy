class Song:
	def __init__(self, name, withArtist, cover, info, tape):
		'''
			https://api.setlist.fm/docs/1.0/json_Song.html
			parameters:
				- name - (String) name of the song
				- withArtist - (Artist) different Artist than the performing one that joined the stage for this song
				- cover - (Artist) the original Artist of this song, if different than performing artist
				- info - (String) special incidents or additional information about the way the song was performed at this specific concert
				- tape - (Boolean) the song came from tape rather than being performed live
		'''
		self.name = name
		self.withArtist = withArtist
		self.cover = cover
		self.info = info
		self.tape = tape