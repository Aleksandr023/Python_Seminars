#18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
from tkinter import Y
from random import randrange

x = randrange(0, 1)
y = randrange(0, 1)
print(not(x or y) == (not x) and (not y))






