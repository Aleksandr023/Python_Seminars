#12. Удалить вторую цифру трёхзначного числа
n = int(input('N = '))
print(n//100*10 + n%10)