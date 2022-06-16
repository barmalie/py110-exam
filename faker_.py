import random
from random import choice,sample

from faker import Faker

fake = Faker()

for _ in range(3):
  population = []
  name = fake.name()
  population.append(name)



 

Faker.seed(0)
for _ in range(5):
  fake.isbn13()





