class Setlists:
	def __init__(self, setlist, total, page, itemsPerPage):
		'''
			https://api.setlist.fm/docs/1.0/json_Setlists.html
			parameters:
				- setlist - (array of Setlist) result list of setlists
				- total - (Int) total amount of items matching the query
				- page - (Int) current page
				- itemsPerPage - (Int) amount of items per page
		'''
		self.setlist = [x for x in setlist]
		self.total = total
		self.page = page
		self.itemsPerPage = itemsPerPage