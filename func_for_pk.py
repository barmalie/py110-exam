#
# def my_range(first=1, last=10, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step
#
#
# my_range()
#
# ranger = my_range(1, 11)
# #print(ranger)
# for x in ranger:
#     print(x)


my_gen_func = count(100, 10)
for _ in range(10):
    print(next(my_gen_func))
