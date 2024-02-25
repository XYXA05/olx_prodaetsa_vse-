def individual_serial(items_search) -> dict:
    return{
        'id':str(items_search['_id']),
        'model': items_search.get('model', ''),
        'price_hight':items_search.get('price_hight',''),
        'price_low': items_search.get('price_low', ''),
        'use': items_search.get('use', ''),
        'city': items_search.get('city', ''),
    }

def list_serilazer(items_searchs) -> dict:
    return[individual_serial(items_search) for items_search in items_searchs] 



def individual_serial_for_item(item) -> dict:
    return{
        'id':str(item['_id']),
        'url':item.get('url', ''),
        'name_url':item.get('name_url', ''),
        'price_url':item.get('price_url', ''),
        'meet_url':item.get('meet_url', ''),
        'items_search_id':item.get('items_search_id','')
    }

def list_serilazer_for_item(items) -> dict:
    return[individual_serial_for_item(item) for item in items]