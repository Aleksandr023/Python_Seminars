#13. Выяснить, кратно ли число заданному, если нет, вывести остаток.

#from random import randrange
a = 5 #randrange(0,100)
b = int(input('enter your number: '))
if b % a == 0:
    print(f'{b} is a multiple of {a}')
else:
    print(f'the remainder of dividing {b} by {a} = ',(b%a))