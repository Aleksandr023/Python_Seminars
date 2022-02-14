#20. Задать номер четверти, показать диапазоны для возможных координат
quarter = int(input("enter quarter number: "))
if quarter == 1:
    print("X > 0, Y > 0")
elif quarter == 2:
    print("X < 0, Y > 0")
elif quarter == 3:
    print("X < 0, Y < 0")
elif quarter == 4:
    print("X > 0, Y < 0")
else:
    print("it's only four quarters, man")



