# Напишите программу, котороая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (х и у).

x = int(input('Введите координаты точки по X: '))

y = int(input('Введите координаты точки по Y: '))

 

if x != 0 and y != 0:

    if x > 0 and y > 0:

        print('1 четверть')

    elif x < 0 and y > 0:

        print('2 четверть')

    elif x < 0 and y < 0:

        print('3 четверть')

    else:

        print('4 четверть')

else:

    print('Введите координаты не равные 0!!!')

 

 

x = int(input('Введите коорддинату Х = '))

y = int(input('Введите коорддинату Y = '))

 

if x > 0:

    if y > 0:

        print(' -> 1')

    else:

        print(' -> 4')       

elif x < 0:

    if y > 0:

        print(' -> 2')

    else:

        print(' -> 3')