# 3. По заданному номеру дня недели вывести его название

daysOfWeek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
n = int(input('enter number of day: '))-1
if n >= len(daysOfWeek):
    print('incorrect input data')
else:
    print(daysOfWeek[n])



