import pymongo

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['recommender']

mongo_query = db['userswithratings'].insert({
        'user': 'anil',
        'movie_rating_scale' : 5,
		'movie_ratings': {
			'captain america' : 4.5,
			'iron man': 5,
			'avengers' : 5,
			'spiderman': 3.5,
			'batman' : 4.5,
			'one night in paris': 2.5,
			'snakes on a plane' : 1.5,
			'superman series' : 4.5
		},
		'tvshow_rating_scale' : 5,
		'tvshow_ratings' : {
			'big bang theory' : 4.5,
			'breaking bad' : 3.5,
			'dexter' : 4.5,
			'daredevil' : 3,
			'game of thrones' : 5,
			'suits' : 4.5,
			'homeland' : 3.5
		},
		'game_rating_scale' : 10,
		'games_ratings' : {
			'max payne': 8,
			'call of duty 1' : 7,
			'GTA 5' : 8,
			'halo' : 6
	}
        })