a = int(input('a = '))
b = int(input('b = '))
if (a == b**2):
    print (a, 'является квадратом', b)
elif (b == a**2):
    print (b, 'является квадратом', a)
else:
    print('ни одно число не является квадратом другого')
