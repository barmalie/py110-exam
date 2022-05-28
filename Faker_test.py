from random import randint
from faker import Faker

fake = Faker()

#fake.name()
for _ in range(3):
  print(fake.name())

Faker.seed(0)
_ =randint(1,100)
print(fake.isbn13())
