#19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0
#from random import randrange
#x = randrange(-10, 11)
#y = randrange(-10, 11)

x = float(input("enter coordinate X = "))
y = float(input("enter coordinate Y = "))
if (x != 0 and y != 0):
    if x > 0 and y > 0:
        print("it's 1'st quarter")
    elif x < 0 and y > 0:
        print("it's 2'nd quarter")
    elif x < 0 and y < 0:
        print("it's 3'rd quarter")
    else: print("it's 4'th quarter")










