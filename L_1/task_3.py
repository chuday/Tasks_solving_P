# Напишите программу которая будет на вход принимать число N и выводить число от -N до N
# 5   -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

num = int(input("Введите число: "))
print(list(range(-num, num+1)))

numb = int(input("Введите число: "))
rand = list(range(numb * -1, numb +1))
print(rand)