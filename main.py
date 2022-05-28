
import random
import json




# MODEL



text_json1 = """{
    "model": "shop_final.book",
    "pk": 1,
    "fields": {
        "title": "test_book",
        "year": 2020,
        "pages": 123,
        "isbn13": "978-1-60487-647-5",
        "rating": 5,
        "price": 123456.0,
        "author": [
            "test_author_1",
            "test_author_2"
        ]
    }
}"""
MODEL = json.loads(text_json1)

#print(MODEL)
#print(MODEL['model'])
#print(type(MODEL['pk']))
MODEL['pk'] = random.randint(22,45)
MODEL['fields']['year'] = random.randint(1990,2020)
MODEL['fields']['pages'] = random.randint(1,1000)
MODEL['fields']['rating'] = float(random.randint(-5,5))
MODEL['fields']['pages'] = float(random.randint(1,1000))
#print(MODEL['pk'])

new_json = json.dumps(MODEL, indent = 2)
print(new_json)