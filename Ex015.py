#15. Дано число. Проверить кратно ли оно 7 и 23

#from random import randrange
#a = randrange(-10000,10001)
a = int(input('a = '))
if a % 7 == 0 and a % 23 == 0:
    print(f'{a} is a multiple of 7 and 23')
else:
    print(f'{a} is NOT multiple of 7 and 23')