# Напишите программу которая по заданному номеру четверти показывает диапазон возможных
# точек в этой четверти

x = int(input("Введите четверть от 1 до 4: "))

if x == 1:
    print("Диапазон Y > 0, диапазон X > 0")
elif x == 2:
    print("Диапазон Y < 0, диапазон X > 0")
elif x == 3:
    print("Диапазон Y < 0, диапазон X < 0")
elif x == 4:
    print("Диапазон Y > 0,  диапазон X < 0")
else:
    print("Некорректные данные")