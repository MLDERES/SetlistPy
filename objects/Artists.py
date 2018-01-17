class Artists:
	def __init__(self, artist, total, page, itemsPerPage):
		'''
			https://api.setlist.fm/docs/1.0/json_Artists.html
			parameters:
				- artist - (array of Artist) result list of Artists
				- total - (Int) total amount of items matching the query
				- page - (Int) the current page
				- itemsPerPage - (Int) the amount of items per page
		'''
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

