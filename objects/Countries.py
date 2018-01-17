class Countries:
	def __init__(self, country, total, page, itemsPerPage):
		'''
			https://api.setlist.fm/docs/1.0/json_Countries.html
			parameters:
				- country - (array of Country) result list of countries
				- total - (Int) total amount of items that match the query
				- page - (Int) current page
				- itemsPerPage - (Int) amount of items per page
		'''
		self.country = [x for x in country]
		self.total = total
		self.page = page
		self.itemsPerPage = itemsPerPage