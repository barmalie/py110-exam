# def my_range(first=1, last=10, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step
#
#
# my_range()
#
# ranger = my_range(1, 100)
# #print(next(ranger))
#
# for x in ranger:
#     print(x)

# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step
#
# my_gen_func = count(1, 1)
# for _ in range(100):
#     print(next(my_gen_func))

# def grep(pattern):
#     i = 0
#     while True:
#         line = yield  # отличие от генератора
#         if pattern in line:
#             i += 1
#             print(f"Found! Count: {i}")