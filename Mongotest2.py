import pymongo
from pymongo import MongoClient

class StoreObj:
    def __init__(self, chn_num, chn_name, st_num, st_name):
        self.chn_num = chn_num
        self.chn_name = chn_name
        self.st_num = st_num
        self.st_name = st_name

    def getchn_num(self):
        return self.chn_num

    def getchn_name(self):
        return self.chn_name

    def getst_num(self):
        return self.st_num

    def getst_name(self):
        return self.st_name

client = MongoClient('localhost',27017)
db = client.csdb
collection = db.storelist2
AEON_stores = []

for cs in collection.find({'Chain_Nbr': 1}):
    str_info = StoreObj(cs['Chain_Nbr'], cs['Chain_Name_J'], cs['Store_Nbr'], cs['Store_Name_J'])
    AEON_stores.append(str_info)

for c in AEON_stores:
    print c.getchn_name()
