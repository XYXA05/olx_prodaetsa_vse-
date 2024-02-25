from fastapi import APIRouter, HTTPException, Depends
from models import Items_Search, Item
from database import collection_name, collection_name1
from schemas import list_serilazer, list_serilazer_for_item
from bson import ObjectId
from findes import Logs
from fastapi import BackgroundTasks
import asyncio




router = APIRouter()
router1 = APIRouter()

@router.get('/get_item_search/')
async def get_items_serch():
    items_serchs = list_serilazer(collection_name.find())
    return items_serchs

@router.post('/fer/')
async def post_items_serch(items_search:Items_Search):
    collection_name.insert_one(dict(items_search))

@router.put('/{id}')
async def put_item_search(id: str, items_search: Items_Search):
    print(f"Received data for ID {id}: {items_search}")
    collection_name.find_one_and_update({'_id': ObjectId(id)}, {"$set": dict(items_search)})

@router.delete('/{id}_item/')
async def delate_item_search(id:str):
    collection_name.find_one_and_delete({'_id':ObjectId(id)})

####
    
@router1.get('/get_save_link/')
async def get_items_serch():
    items_serchs = list_serilazer_for_item(collection_name1.find())
    return items_serchs



stop_processing = {}

async def process_item(item_url, collection_name, item_id):
    item_data = {
        "name_url": item_url["name_url"],
        "price_url": item_url["price_url"],
        "meet_url": item_url["meet_url"],
        "url": item_url["url"],
        "items_search_id": item_url["items_search_id"]
    }
    item = Item(**item_data)
    collection_name.insert_one(item.dict())
    print(f"Item processed for ID {item_id}")

# ...
async def periodic_task(item_id):

    while True:

        iphone_list = await Logs.log(item_id)

        for item_url in iphone_list:
            if stop_processing.get(item_id, False):
                return {"message": f"Processing stopped for ID {item_id}"}

            # Directly call the coroutine function with the required arguments
            await process_item(item_url, collection_name1, item_id)
        use = collection_name.find_one({"_id": ObjectId(item_id)})
        await asyncio.sleep(use['use'])

# ...

@router1.post('/save_link_on_olx/')
async def post_items_search(data: dict, background_tasks: BackgroundTasks):

    global stop_processing

    item_id = data.get('id')
    
    # Start the periodic task in the background
    background_tasks.add_task(periodic_task, item_id)

    return {"message": f"Periodic task started for ID {item_id}"}

@router1.post('/stop_processing/')
async def stop_processing_route(data: dict):
    item_id_stop = data.get('id')
    global stop_processing
    stop_processing[item_id_stop] = True
    return {"message": f"Processing will be stopped for ID {item_id_stop}"}






@router1.put('/{id}_items/')
async def put_item_search(id:str, items_search:Item):
    collection_name1.find_one_and_update({'_id': ObjectId(id)}, {"$set": dict(items_search)})

@router1.delete('/{id}_items')  
async def delate_item_search(id:str):
    collection_name1.find_one_and_delete({'_id':ObjectId(id)})
