#Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
from random import randrange
a = randrange(10,100)
print(a)
if a // 10 == a % 10:
    print('the digits of the number are equal')
else:
    print(max(a//10, a%10))

