#26. Возведите число А в натуральную степень B используя цикл

a = int(input("A = "))
b = int(input("B = "))
result = 1
for i in range(1, b+1):
    result = result * a
print(result)