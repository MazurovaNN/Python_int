# Задача 1. Напишите программу, которая принимает на вход вещественное 
# показывает сумму его цифр. 
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = float(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input

# здесь если число дробное, сначала переводим его в целое до последнего
# знака после запятой 
# но возникает проблема - в случае с 0,56 или 4,56 например, 
# появляются "лишние" цифры в типе float и результат неверный.
# для округления надо воспользоваться длиной строки.

def sum_digits(number):
    # число знаков после точки
    znakov = (len(str(number))-len(str(int(number)))-1) 
    number = round(number, znakov)
    print(f'Первое округление до цикла приведения к целому:     {number}')

    while number % 1 != 0: 
        znakov-=1 #с каждым циклом число знаков после запятой сокращается на 1
        number= round(number*10, znakov)

    number = int(number)    
    print(f'Целое число для расчетов: {number}')

    sum_digits = 0
    while number != 0: 
        sum_digits += number % 10 
        number//=10
    
    return sum_digits  