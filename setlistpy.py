# Wrapper for Setlist.FM's API
import requests
import json

class SetlistPy:
	def __init__(self):
		headers = {
			'Accept': 'application/json'
		}
	


#SETLIST.FM -- search for artist
	headers = {
		'Accept': 'application/json',
		'x-api-key': SETLIST_FM_API_KEY
	}
	context['query'] = getQueryFromSetlistFM(headers, context)

# get artist's first page of setlists
artist_search_url   = 'https://api.setlist.fm/rest/1.0/search/artists?artistName={}&p=1&sort=sortName'
	artist_search_query = artist_search_url.format(context['artist'])
	r = requests.get(artist_search_query, headers=headers)
	return r.json()