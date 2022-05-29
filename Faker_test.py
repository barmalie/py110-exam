from random import choice
from faker import Faker

fake = Faker()

for _ in range(3):
  name = fake.name()
  name_2 = fake.name()
  # name_3 = fake.name()
  #name = name.split(',')
  # name_2 = name_2.split(',')
  # name_3 = name_3.split(',')
  choice_name = choice(name)
  choice_name_2 = choice(name_2)
  # choice_name_3 = choice(name_3)
  print(name)
  print(name_2)

Faker.seed(100)

for identification_number in range(5):
  index_book = fake.isbn13()
  # for i in index_book:
  index_book = index_book.split(',')
  choice_index = choice(index_book)
  print(choice_index)