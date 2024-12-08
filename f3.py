def f3(x, y):
    for i in range(1, y):
        print('x hat',x)
        print('i hat',i)
        x.append(i)
        print('Innen',x)
x=[5, 6, 7 ,8]
y=10
print('Aussen_1', x)
f3(x,y)
print('Aussen_2', x)
