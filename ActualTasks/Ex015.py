# 15. Написать программу получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

n = int(input("N = "))
list = []
a = 1
for i in range(1, n+1):
    list.append(i*a)
    a = list[i-1]
print(list)






