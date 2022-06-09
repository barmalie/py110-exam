import random
import json

import model
import faker_


# MODEL = json.loads(model.MODEL_)
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


@repeat(10)
def main():
    """
    ОСНОВНАЯ ФУНКЦИЯ ЗАПУСКА ПРОГРАММЫ
    :return:
    """
    MODEL = json.loads(model.MODEL_)

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

    @repeat()
    def modul_pk(start=1, step=1):
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

    def model_year():
        """
        РАНДОМНОЕ УКАЗАНИЕ ГОДА
        :return:
        """
        MODEL['fields']['year'] = random.randint(1990, 2020)
        return

    model_year()

    def model_pages():
        """
        СЛУЧАЙНОЕ УКАЗАНИЕ СТРАНИЦЫ
        :return:
        """
        MODEL['fields']['pages'] = random.randint(1, 1000)
        return

    model_pages()

    def model_rating():
        """
        СЛУЧАЙНОЕ УКАЗАНИЕ РЕЙТИНГА В ДИАПАЗОНЕ ОТ -5 ДО 5
        :return:
        """
        MODEL['fields']['rating'] = float(random.randint(-5, 5))
        return

    model_rating()

    def modul_isbn13():
        """
        ИДЕНТИФИКАЦИОННЫЙ НОМЕР КНИГИ ПО ISBN13
        :return:
        """
        MODEL['fields']['isbn13'] = faker_.fake.isbn13()
        return

    modul_isbn13()

    def modul_title():
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

    def model_year():
        """
        СЛУЧАЙНЫЙ ГОД
        :return:
        """
        MODEL['fields']['year'] = random.randint(1990, 2020)
        return

    model_year()

    def model_pages():
        """
        СЛУЧАЙНАЯ СТРАНИЦА
        :return:
        """
        MODEL['fields']['pages'] = random.randint(1, 1000)
        return

    model_pages()

    def model_rating():
        """
        ПРОИЗВОЛЬНЫЙ РЕЙТИНГ
        :return:
        """
        MODEL['fields']['rating'] = float(random.randint(-5, 5))
        return

    model_rating()

    def model_price():
        """
        СЛУЧАЙНАЯ ЦЕНА
        :return:
        """
        MODEL['fields']['price'] = float(random.randint(1, 1000))
        return

    model_price()

    def author():
        """
        СЛУЧАЙНЫЙ АВТОР №1
        :return:
        """
        MODEL['fields']['author'][1] = faker_.fake.name()
        return

    author()

    def author_2():
        """
        СЛУЧАЙНЫЙ АВТОР №2
        :return:
        """
        MODEL['fields']['author'][0] = faker_.fake.name()
        return

    author_2()

    with open('copy.py', 'w', encoding='utf8') as f:
        json.dumps(MODEL, indent=2, ensure_ascii=False)
        print(json.dumps(MODEL, indent=2, ensure_ascii=False))
        MODEL = json.dumps(model.MODEL_)


if __name__ == "__main__":
    main()
