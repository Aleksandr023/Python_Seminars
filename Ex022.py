#22. Найти расстояние между точками в пространстве 2D/3D
from random import randrange
#from math import *
x1 = float(randrange(-10, 11))
y1 = float(randrange(-10, 11))
x2 = float(randrange(-10, 11))
y2 = float(randrange(-10, 11))
z1 = float(randrange(-10, 11))
z2 = float(randrange(-10, 11))

#print(f"2D distance: sqrt (({x2} - {x1})^2 + ({y2} - {y1})^2) = ", sqrt ((x2-x1)**2+(y2-y1)**2))
#print(f"3D distance: sqrt (({x2} - {x1})^2 + ({y2} - {y1})^2 + ({z2} - {z1})^2) = ", sqrt ((x2-x1)**2+(y2-y1)**2)+(z2-z1)**2)

print(f"2D distance: sqrt (({x2} - {x1})^2 + ({y2} - {y1})^2) = ", ((x2-x1)**2+(y2-y1)**2)**0.5)
print(f"3D distance: sqrt (({x2} - {x1})^2 + ({y2} - {y1})^2 + ({z2} - {z1})^2) = ", ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**0.5) #без библиотеки math(вычисление квадратного корня **0.5)
