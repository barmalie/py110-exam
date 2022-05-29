def my_range(first=1, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


my_range()

ranger = my_range(1, 5)
print(next(ranger))
print(next(ranger))


def count(start=1, step=1):
    counter = start
    while True:
        yield counter
        counter += step

my_gen_func = count(100, 10)
for _ in range(10):
    print(next(my_gen_func))