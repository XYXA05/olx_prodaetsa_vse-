import certifi
from pymongo import MongoClient


client = MongoClient('******************************', tlsCAFile=certifi.where())
db = client.todo_db

collection_name = db['items_olx']   
collection_name1 = db['items_get_olx']
