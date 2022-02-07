#  4. Найти максимальное из трех чисел
from random import randrange
a = randrange(0, 100)
b = randrange(0, 100)
c = randrange(0, 100)
print(a,b,c)
if a>b>c:
    print('Максимальное число', a)
elif b>a>c:
    print('Максимальное число', b)
else:
    print('Максимальное число', c)



#list = []
#for i in range(3):
#    a = int(input())
#    list.append(a)
#print(max(list))
