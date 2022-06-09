# def count(start=1, step=1):
#     MODEL['pk'] = start
#     while True:
#         yield MODEL['pk']
#         MODEL['pk'] += step
#
#
# MODEL['pk'] = count()
# for _ in range(10):
#
#     #MODEL['pk'] = ranger
#     print(next(MODEL['pk']))
#
# modul_pk()

def iter_(start=1,step=1):
    #count = start
    for i in range(1,21):
        yield i
        #count += step

# count_pk = iter_()
# print(next(count_pk))
# print(next(count_pk))

for i in iter_():
    print(i)