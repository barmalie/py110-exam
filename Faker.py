import json

from faker import Faker


from faker.providers import internet
# fake = Faker('it_IT')
# fake = Faker('ru_RU')
for fake in range(200):
    print(fake.name())

#     print(fake.simple_profile())
    print(fake.isbn13())
#     print(fake.job())
#     print(fake.name())
#     print(fake.telephone_number())
f = open("requirement.txt", 'w')

dict = {}
fake = Faker()
# fake.add_provider(internet)
#
# print(fake.ipv4_private())

fake.job()
fake.phone_number()
fake.name()

for i in (range(200)):
    name = fake.name()
    phone = fake.phone_number()
    job = fake.job()
    dict[i] = {i:[name,phone,job]}
    with open('DS.txt', 'w', encoding ='utf8') as f:
            json.dump(dict,f,indent=4,ensure_ascii=False)
    # print(index,fake.name(),fake.phone_number(),fake.job())
    # print(index,name,.phone_number,job)
  # for index in :
  #     f.write(index + '\n')


# f.write()
# f.close()

  # print(fake.phone_number())
  # print(fake.job())

# fake = Faker(['it_IT', 'en_US', 'ja_JP'])
# # for _ in range(10):
# #     print(fake.name())
#
# # fake = Faker()
# # fake.random
# # fake.random.getstate()
