#27. Определить количество цифр в числе
a = int(input("A = "))

#str_a = str(a)
#print(len(str_a))

digits = 0
while (a > 0):
    digits +=1
    a = a // 10
print(digits)




