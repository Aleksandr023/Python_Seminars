#5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

a = int(input('a = '))
if (a % 30 != 0):
    if (a % 5 == 0):
        if(a % 10 == 0):
            print('число удовлетворяет условиям')
        elif (a % 15 == 0):
            print('число', a, 'удовлетворяет условиям')
    else:
        print('число', a, 'не удовлетворяет условиям')
else:
    print('число', a, 'не удовлетворяет условиям')