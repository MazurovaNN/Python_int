# 1. Вычислить число c заданной точностью *d* 
# *Пример:*  
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$ 

from math import pi 
d =  input('Введите число для заданной точности числа Пи: ') 

d = len(str(d).split('.')[1]) 

print(f'число Пи с заданной точностью "{d} знак" равно {round(pi, d)}') 