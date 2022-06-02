def count(start=1, step=1):
    MODEL['pk'] = start
    while True:
        yield MODEL['pk']
        MODEL['pk'] += step


# ranger = modul_pk(1, 1)
# for _ in range(10):
#     #MODEL['pk'] = next(ranger)
#     MODEL['pk'] = ranger

modul_pk()