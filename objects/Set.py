class Set:
	def __init__(self, name, encore, song):
		'''
			https://api.setlist.fm/docs/1.0/json_Set.html
			parameters:
				- name - (String) the description/name of the set
				- encore - (Int) if the set is an encore, this is the number of the encore
				- song - (array of Song) this set's songs
		'''
		self.name = name
		self.encore = encore
		self.song = song