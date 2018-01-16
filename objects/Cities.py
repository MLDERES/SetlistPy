class Cities:
	def __init__(self, cities, total, page, itemsPerPage):
		self.cities = [x for x in cities]
		self.total = total
		self.page = page
		self.itemsPerPage = itemsPerPage