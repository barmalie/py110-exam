from random import randint
from faker import Faker

fake = Faker()

#fake.name()
for _ in range(3):
  print(fake.name())

Faker.seed(0)
#identification_number = randint(1, 1000)
for identification_number in range(5):
  print(fake.isbn13())
