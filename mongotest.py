import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient('localhost',27017)

db = client.csdb
collection = db.storelist2

#for s in collection.find():
#    print s['Store_Name_J']

#print collection.count()

for s in collection.find({'Chain_Nbr': 1}):
  print s['Store_Nbr'], s['Store_Name_J']  

print (collection.find_one({'Chain_Nbr': 1}))

# print s['Chain_Nbr'], s['Store_Nbr'], s['Store_Name_J']

# print collection.find_one({'Chain_Nbr':1})