import certifi
from pymongo import MongoClient


client = MongoClient('mongodb+srv://bogdansavi05:iAcMgXdOvohD5ly3@olx.4p6lijm.mongodb.net/', tlsCAFile=certifi.where())
db = client.todo_db

collection_name = db['items_olx']   
collection_name1 = db['items_get_olx']