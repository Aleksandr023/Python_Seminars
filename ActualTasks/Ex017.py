# 17. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число
list = []
n = int(input('N = '))
for i in range (-n, n+1):
    list.append(i)
#print(list)

res = 1
with open('Ex017.txt', 'r') as data:
    for line in data:            
        i = int(line)
        if i > len(list):                   
            print("список слишком короткий")
        else:
            res = res * list[i]
print(res)

# res = 1
# path = 'Ex017.txt'
# data = open(path, 'r')
# for line in data:
#     i = int(line)
#     #print(line)
#     res = res * list[i]
# data.close()
# print(res)












