import random
import json

import conf
#import Faker_test

def main():
    text = open('BOOK.txt', 'r', encoding='utf8')
    for i in text:
        print(i)
        text.close()

MODEL = json.loads(conf.text_json1)


# print(MODEL)
# print(MODEL['model'])
# print(type(MODEL['pk']))
# def my_range(first=1, step=1):

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

new_json = json.dumps(MODEL, indent=2)
print(new_json)
