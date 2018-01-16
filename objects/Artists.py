class Artists:
	def __init__(self, artist, total, page, itemsPerPage):
		self.artist = [x for x in artist]
		self.total = total
		self.page = page
		self.itemsPerPage = itemsPerPage

	def getArtistList():
		return self.artist

	def getTotal():
		return self.total

	def getPage():
		return self.page

	def getItemsPerPage():
		return self.itemsPerPage

