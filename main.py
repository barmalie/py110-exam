import random
import json

import copy
import model
import faker_

def repeat(number=17):
    """
    ФУНКЦИЯ-ДЕКОРАТОР СЧЕТЧИКА ДЛЯ MAIN
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


@repeat(100)
def main() -> str:
    """
    ОСНОВНАЯ ФУНКЦИЯ ЗАПУСКА ПРОГРАММЫ
    :return:
    """
    MODEL = json.loads(model.MODEL_)

    def modul_title() -> str:
        """
        СЛУЧАЙНЫЙ ВЫБОР КНИГИ
        :return:
        """
        text = open('BOOK.txt', 'r', encoding='utf8')
        s = text.readline()
        book = s.split(',')
        book_ = random.choice(book)
        book_2 = random.choice(book)
        MODEL['fields']['title'] = book_ + ',' + book_2

    modul_title()

    @repeat()
    def modul_pk(start=1, step=1) -> int:
        """
        АВТОИНКРЕМЕНТНЫЙ СЧЕТЧИК ПОДСЧЕТА ВЫЗОВОВ ДАННЫХ
        :return:
        """
        n = start
        while True:
            yield n
            n += step

    ranger = modul_pk()
    for _ in range(11):
        MODEL['pk'] = next(ranger)

    modul_pk(10, 1)

    def model_year() -> int:
        """
        РАНДОМНОЕ УКАЗАНИЕ ГОДА
        :return:
        """
        MODEL['fields']['year'] = random.randint(1990, 2020)
        return

    model_year()

    def model_pages() -> int:
        """
        СЛУЧАЙНОЕ УКАЗАНИЕ СТРАНИЦЫ
        :return:
        """
        MODEL['fields']['pages'] = random.randint(1, 1000)
        return

    model_pages()

    def model_rating() -> float:
        """
        СЛУЧАЙНОЕ УКАЗАНИЕ РЕЙТИНГА В ДИАПАЗОНЕ ОТ -5 ДО 5
        :return:
        """
        MODEL['fields']['rating'] = float(random.randint(-5, 5))
        return

    model_rating()

    def modul_isbn13() -> str:
        """
        ИДЕНТИФИКАЦИОННЫЙ НОМЕР КНИГИ ПО ISBN13
        :return:
        """
        MODEL['fields']['isbn13'] = faker_.fake.isbn13()
        return

    modul_isbn13()

    def modul_title() -> str:
        """
        НАЗВАНИЕ КНИГИ ЭКСПОРТИРОЕМОЕ ИЗ ТЕКСТОВОГО ФАЙЛА
        :return:
        """
        text = open('BOOK.txt', 'r', encoding='utf8')
        s = text.readline()
        book = s.split(',')
        book_ = random.choice(book)
        book_2 = random.choice(book)
        MODEL['fields']['title'] = book_ + ',' + book_2

    modul_title()

    def model_year() -> int:
        """
        СЛУЧАЙНЫЙ ГОД
        :return:
        """
        MODEL['fields']['year'] = random.randint(1990, 2020)
        return

    model_year()

    def model_pages() -> int:
        """
        СЛУЧАЙНАЯ СТРАНИЦА
        :return:
        """
        MODEL['fields']['pages'] = random.randint(1, 1000)
        return

    model_pages()

    def model_rating() -> float:
        """
        ПРОИЗВОЛЬНЫЙ РЕЙТИНГ
        :return:
        """
        #MODEL['fields']['rating'] = float(random.randint(-5, 5))
        MODEL['fields']['rating'] = random.triangular(-5, 4, 7)
        return

    model_rating()

    def model_price() -> float:
        """
        СЛУЧАЙНАЯ ЦЕНА
        :return:
        """
        MODEL['fields']['price'] = float(random.randint(1, 1000))
        return

    model_price()

    def autor() -> str:
        """
        ВЫБОР СЛУЧАЙНОГО АВТОРА
        :return:
        """

        def autor1() -> str:
            MODEL['fields']['author'][0] = faker_.fake.name()

        def autor2() -> str:
            MODEL['fields']['author'][0] = faker_.fake.name()
            MODEL['fields']['author'][1] = faker_.fake.name()

        def autor3() -> str:
            MODEL['fields']['author'][0] = faker_.fake.name()
            MODEL['fields']['author'][1] = faker_.fake.name()
            MODEL['fields']['author'][2] = faker_.fake.name()

        list = [autor1(), autor2(), autor3()]
        for i in list:
            return i

    autor()

    with open('copy.py', 'w', encoding='utf8') as f:
        json.dumps(MODEL, indent=2, ensure_ascii=False)
        print(json.dumps(MODEL, indent=2, ensure_ascii=False))

    f.close()


if __name__ == "__main__":
    main()
