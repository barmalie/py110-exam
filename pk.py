def count(start=1, step=1):
    MODEL['pk'] = start
    while True:
        yield MODEL['pk']
        MODEL['pk'] += step


MODEL['pk'] = count()
for _ in range(10):

    #MODEL['pk'] = ranger
    print(next(MODEL['pk']))

modul_pk()