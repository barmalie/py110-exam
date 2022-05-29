import random
import json

import conf
import Faker_test

MODEL = json.loads(conf.text_json1)

def main():
    def count():
        new_json = json.dumps(MODEL, inden=2, ensure_ascii=False)
        pr = new_json
        for i in range(1, 10):
            yield pr

        def modul_title():
            text = open('BOOK.txt', 'r', encoding='utf8')
            s = text.readline()
            book = s.split(',')
            book_ = random.choice(book)
            book_2 = random.choice(book)
            MODEL['fields']['title'] = book_ + ',' + book_2


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


        def modul_isbn13():
            MODEL['fields']['isbn13'] = Faker_test.index_book
            return


        modul_isbn13()


        def model_price():
            MODEL['fields']['price'] = float(random.randint(1, 1000))
            return


        model_price()


        def author():
            MODEL['fields']['author'][1] = Faker_test.name
            MODEL['fields']['author'][0] = Faker_test.name_2
        return


        author()


    # new_json = json.dumps(MODEL, indent=2, ensure_ascii=False)
    # print(new_json)
        s = count()
        print(next(s))



    # new_json = json.dumps(MODEL, inden=2, ensure_ascii=False)
    # print(new_json)

    # def count(start=1, step=1):
    #     counter = start
    #     while True:
    #         yield counter
    #         counter += step
    #
    # new_json = count(1, 1)
    # for x in new_json(100):
    #     print(x)
    return  # new_json*100





if __name__ == "__main__":
    main()