class User:
	def __init__(self, userId, fullName, lastFm, mySpace, twitter, flickr, website, about, url):
		'''
			https://api.setlist.fm/docs/1.0/json_User.html
			parameters:
				- userId - (String)
				- fullName - (String)
				- lastFm - (String)
				- mySpace - (String)
				- twitter - (String)
				- flickr - (String)
				- website - (String)
				- about - (String)
				- url - (String)
		'''
		self.userId = userId
		self.fullName = fullName
		self.lastFm = lastFm
		self.mySpace = mySpace
		self.twitter = twitter
		self.flickr = flickr
		self.website = website
		self.about = about
		self.url = url