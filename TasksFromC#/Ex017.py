#17. По двум заданным числам проверять является ли одно квадратом другого
a = int(input("enter 1'st number: "))
b = int(input("enter 2'nd number: "))
if a ** 2 == b:
    print(f"{b} is the square of {a}")
elif b ** 2 == a:
    print(f"{a} is the square of {b}")
else:
    print("neither number is the square of the other")



