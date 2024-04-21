from pymongo import MongoClient

client = MongoClient('localhost', 27017, username='root', password='example')

db = client['posts']
posts_collection = db['posts']
posts_collection.drop()