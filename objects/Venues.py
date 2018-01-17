class Venues:
	def __init__(self, venue, total, page, itemsPerPage):
		'''
			https://api.setlist.fm/docs/1.0/json_Venues.html
			parameters:
				- venue - (array of Venue) result list of venues
				- total - (Int) total amount of items that match the query
				- page - (Int) current page
				- itemsPerPage - (Int) amount of items per page
		'''
		self.venue = [x for x in venue]
		self.total = total
		self.page = page
		self.itemsPerPage = itemsPerPage