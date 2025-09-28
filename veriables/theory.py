# name = 'Alice'
# age = 25
# print('name, age')


# x = 3 
# y = 4

# x, y = y, x
# print(x, y)



# str-строка
# variable = 'Hello, world'
# print(type(variable))


# преобразовать строку в целое число можно командой/функцией int()
# s = '1992'
# year = int(s)

# print(year)



# что бы через input() ввести число нужно добавить функцию int() , а то программа считает введенные данные как текст , а не число 
# num1 = int(input())
# num2 = int(input())

# print(num1 + num2)



# преобразование целого числа к строке делается с помощью функции str()
# num = 17
# s = str(num)



# int-числа
# my_integer = 10 # целые числа
# my_float = 20.5 # с плавающей точкой



# INTEGER - целые числа
# x = 10
# y = 5
# summery = x + y

# print(summery)



#FLOAT - числа с плавающей точкой/дробные
# x = 7.3
# y = 10.9
# summery = x + y

# print(summery)



# x = 5
# y = 5
# z = x * y

# print(type(z))
# УМНОЖЕНИЕ БУДЕТ ТИПА INTEGER



# x = 5
# y = 5
# z = x / y
# print(type(z))
# ДЕЛЕНИЕ БУДЕТ ТИПА FLOAT



# НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ . ВЫДАЕТ ОШИБКУ



# ** возведение в степень 
# // целочисленное деление 
# % остаток от деления

# ВОЗВЕДЕНИЕ В СТЕПЕНЬ 3
# x = 3 
# print(x ** 3)


# ЦЕЛОЧИСЛЕННОЕ ДЕЛЕНИЕ
# x = 9
# y = 4

# print(x // y)


#ОСТАТОК ОТ ДЕЛЕНИЯ
# x = 9
# y = 4

# print(x % y)



# integer можно складывать с float. в таком случае мы получим число типа float
# my_integer = 10
# my_float = 5.5

# print(my_integer + my_float)


# int не округляет , а просто отрезает все что после точки
# my_float = 1.9999
# my_integer = int(my_float)

# print(my_integer)


#что бы округлить используем функцию round
# my_float = 1.9999
# my_integer = round(my_float)

# print(my_integer)



# ТИП BOOL
# ВКЛЮЧАЕТ В СЕБЯ 2 ЗНАЧЕНИЯ True или False
# is_student = True
# is_graduated = False

# print(is_graduated)



# результатом будет переменная типа bool(True или False)
# оператор сравнения/равенства ==
# x = 10
# y = 10
# print(x == y)



# оператор сравнения/равенства ==
# оператор не равенства !=
# больше >
# меньше <
# больше либо равно >=
# меньшк либо равно <=



# x = 10
# y = 9
# print(x > y) # True
# print(x < y) # False
# print(x == y) # False
# print(x >= y) # True
# print(x <= y) # False


# x = 10
# y = 10

# print(x >= y) # True
# print(x <= y) # True


# для проверки двух условий используем операторы and и or

# x = 6
# print(x < 5 and x > -2)

# оператор not меняет знак у переменной типа bool
# is_student = True
# print(not is_student)


