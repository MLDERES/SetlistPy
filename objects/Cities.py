class Cities:
	def __init__(self, cities, total, page, itemsPerPage):
		'''
			https://api.setlist.fm/docs/1.0/json_Cities.html
			parameters:
				- cities - (array of City) result list of cities
				- total - (Int) total amount of items matching the query
				- page - (Int) the current page
				- itemsPerPage - (Int) amount of items per page
		'''
		self.cities = [x for x in cities]
		self.total = total
		self.page = page
		self.itemsPerPage = itemsPerPage