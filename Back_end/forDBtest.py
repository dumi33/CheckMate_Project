from doctest import DocTest
import pymongo

conn = pymongo.MongoClient()
mydb = conn.CHECKMATE
User = mydb.Users

docs = User.find({'id':{'$eq' : 423}})
print(len(list(docs)))
