
from random import choice

from faker import Faker

fake = Faker()
population = []
for _ in range(3):

  name = fake.name()
  population.append(name)
  name_choice = choice(population, 2)
  print(name_choice)
 

Faker.seed(0)
for _ in range(5):
  fake.isbn13()


