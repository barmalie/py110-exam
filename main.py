import random
import json

import conf
import Faker_test


MODEL = json.loads(conf.text_json1)


def repeat(number=1000):
    """

    :param number:
    :return:
    """
    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for iter in range(number):
                result = function(*args, **kwargs)
            return result

        return wrapper

    return actual_decorator


@repeat()
def main():
    """

    :return:
    """
    def modul_title():
        """

        :return:
        """
        text = open('BOOK.txt', 'r', encoding='utf8')
        s = text.readline()
        book = s.split(',')
        book_ = random.choice(book)
        book_2 = random.choice(book)
        MODEL['fields']['title'] = book_ + ',' + book_2

    modul_title()

    def modul_pk(start=1, step=1):
        """

        :param start:
        :param step:
        :return:
        """
        counter = start
        while True:
            yield counter
            counter += step

    ranger = modul_pk(1, 1)
    for _ in range(10):
        MODEL['pk'] = next(ranger)

    modul_pk()

    def model_year():
        """

        :return:
        """
        MODEL['fields']['year'] = random.randint(1990, 2020)
        return

    model_year()

    def model_pages():
        """
    
        :return: 
        """
        MODEL['fields']['pages'] = random.randint(1, 1000)
        return

    model_pages()

    def model_rating():
        """
    
        :return:
        """
        MODEL['fields']['rating'] = float(random.randint(-5, 5))
        return

    model_rating()

    def modul_isbn13():
        """
    
        :return:
        """
        MODEL['fields']['isbn13'] = Faker_test.index_book
        return

    modul_isbn13()

    def modul_title():
        """

        :return:
        """
        text = open('BOOK.txt', 'r', encoding='utf8')
        s = text.readline()
        book = s.split(',')
        book_ = random.choice(book)
        book_2 = random.choice(book)
        MODEL['fields']['title'] = book_ + ',' + book_2

    modul_title()

    def modul_pk(start=1, step=1):
        """

        :param start:
        :param step:
        :return:
        """
        counter = start
        while True:
            yield counter
            counter += step

    ranger = modul_pk(1, 1)
    for _ in range(10):
        MODEL['pk'] = next(ranger)

    modul_pk()

    def model_year():
        """

        :return:
        """
        MODEL['fields']['year'] = random.randint(1990, 2020)
        return

    model_year()

    def model_pages():
        """
    
        :return:
        """
        MODEL['fields']['pages'] = random.randint(1, 1000)
        return

    model_pages()

    def model_rating():
        """

        :return:
        """
        MODEL['fields']['rating'] = float(random.randint(-5, 5))
        return

    model_rating()

    def modul_isbn13():
        """

        :return:
        """
        MODEL['fields']['isbn13'] = Faker_test.index_book
        return

    modul_isbn13()

    def model_price():
        """

        :return:
        """
        MODEL['fields']['price'] = float(random.randint(1, 1000))
        return

    model_price()

    def author():
        """

        :return:
        """
        MODEL['fields']['author'][1] = Faker_test.name
        MODEL['fields']['author'][0] = Faker_test.name_2
        return

    author()

    def model_price():
        """

        :return:
        """
        MODEL['fields']['price'] = float(random.randint(1, 1000))
        return

    model_price()

    def author():
        """

        :return:
        """
        MODEL['fields']['author'][1] = Faker_test.name
        MODEL['fields']['author'][0] = Faker_test.name_2
        return

    author()

    with open('copy.py', 'w', encoding='utf8') as f:
        json.dumps(MODEL, indent=2, ensure_ascii=False)
        print(json.dumps(MODEL, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
