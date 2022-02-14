list = [5,8,555,36,97]
max = list[0]
i = 1
while i < len (list):
    if (max < list[i]):
        max = list[i]
        i+=1
    else:
        i+=1
print (max)