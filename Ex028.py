#28. Подсчитать сумму цифр в числе
a = int(input("a = "))
sum = 0
#for i in range (-a, 0):
#    sum = sum + a%10*
#    a = a//10
#print(sum)
while a>0:
    sum = sum + a%10
    a = a//10
print(sum)


