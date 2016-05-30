import pymongo

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['recommender']

mongo_query = db['userswithratings'].find({})

res = mongo_query

print list(res)