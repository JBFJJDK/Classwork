m = int(input())
if m<=60:
    print('Легкий')
elif m>60 and m<=64:
    print('Первый полусредний')
elif m>64 and m<=69:
    print('Полусредний')
else:
    print('Боксер не подходит ни под одну категорию')
