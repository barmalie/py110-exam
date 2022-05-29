import random
import json

import conf
#import Faker_test

MODEL = json.loads(conf.text_json1)
#def main():
def modul_title():
    #list = []
    text = open('BOOK.txt', 'r', encoding='utf8')
    for name_book in text:
        print(name_book)
        #
        MODEL['fields']['title'] = random(name_book)
        #text.close()

modul_title()

def modul_pk(start=1, step=1):
    counter = start
    while True:
        yield counter
        counter += step

ranger = modul_pk(1, 1)
for _ in range(10):
    MODEL['pk'] = next(ranger)

modul_pk()
def model_year():
    MODEL['fields']['year'] = random.randint(1990, 2020)
    return
model_year()
def model_pages():
    MODEL['fields']['pages'] = random.randint(1, 1000)
    return
model_pages()
def model_rating():
    MODEL['fields']['rating'] = float(random.randint(-5, 5))
    return
model_rating()
def model_price():
    MODEL['fields']['price'] = float(random.randint(1, 1000))
    return
model_price()
# def author():
#MODEL['fileds']['author'] = [Faker_test.fake.isbn13()]
#     return
# author()
# print(MODEL['pk'])

new_json = json.dumps(MODEL, indent=2, ensure_ascii=False)
print(new_json)


# dict[i] = {i:[name,phone,job]}
#     with open('DS.txt', 'w', encoding ='utf8') as f:
#             json.dump(dict,f,indent=4,ensure_ascii=False)