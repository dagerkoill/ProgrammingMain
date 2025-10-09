# ПРОГРАММА ВЫЧИСЛЯЕТ ПЛОЩАДЬ КРУГА И ДЛИНУ ОКРУЖНОСТИ 
# from math import pi, pow


# R = float(input())

# S = pi * (pow(R, 2))
# C = 2 * pi * R

# print(S)
# print(C)




# ПРОГРАММА ИЩЕТ СУМУ ЧИСЕЛ ОКРУГЛЕННЫХ В МЕНЬШУЮ И БОЛЬШУЮ СТОРОНУ 
# from math import floor, ceil


# x = float(input())

# print(floor(x) + ceil(x))




# ПРОГРАММА, КОТОРАЯ ОПРЕДЕЛЯЕТ ЕВКЛИДОВО РАССТОЯНИЕ МЕЖДУ ДВУМЯ ТОЧКАМИ
# from math import sqrt, pow


# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())

# print(sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2)))




# НАПИШИТЕ ПРОГРАММУ, ВЫЧИСЛЯЮЩУЮ ЗНАЧЕНИЕ ТРИГОНОМЕТРИЧЕСКОГО ВЫРАЖЕНИЯ
# from math import pow, radians, sin, cos, tan


# x = radians(float(input()))

# print(sin(x) + cos(x) + pow(tan(x), 2))




# НАПИШИТЕ ПРОГРАММУ ЧТО НАХОДИТ ПЛОЩАДЬ МНОГОУГОЛЬНИКА
# from math import tan, pi


# n = int(input())
# a = float(input())

# print(n * a ** 2 / (4 * tan(pi / n)))




# ПРОГРАММА ЧТО НАХОДИТ 4 СРЕДНИХ ЗНАЧЕНИЯ 
# from math import sqrt


# a = float(input())
# b = float(input())
 
# print((a + b) / 2)
# print(sqrt(a * b))
# print((2 * a * b) / (a + b))
# print(sqrt(a ** 2 + b ** 2 / 2))




# ПРОГРАММА ЧТО НАХОДИТ КОРНИ КВАДРАТНОГО УРАВНЕНИЯ 
# from math import sqrt                 


# a = float(input())
# b = float(input())
# c = float(input())
# D = (b ** 2) - 4 * a * c
# x = -(b / (2 * a))
# x1 = -b - sqrt(D) / (2 * a)
# x2 = -b + sqrt(D) / (2 * a)

# if D < 0:
#     print('Нет корней')
# elif D == 0:
#     print(x)
# elif D > 0:
#     print(f'{x1}\n{x2}')


# from math import sqrt, pow

# a = float(input())
# b = float(input())
# c = float(input())
# D = pow(b, 2) - 4 * a * c

# if D < 0:
#     print('Нет корней')
# elif D == 0:
#     x = -b / (2 * a)
#     print(x)
# elif D > 0:
#     x1 = (-b - sqrt(D)) / (2 * a)
#     x2 = (-b + sqrt(D)) / (2 * a)
#     print(min(x1, x2))
#     print(max(x1, x2))
















