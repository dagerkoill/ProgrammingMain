#                                                 РЕШЕНИЕ ЗАДАЧ 
 
# НАПИСАТЬ ПРОГРАММУ СЧИТЫВАЮЩУЮ ОДНУ СТРОКУ . 
# Задача 1.
# Если это строка «Python», программа выводит «ДА», в противном случае программа выводит «НЕТ».

# ПРОГРАММА РЕШАЮЩАЯ ЭТО МОЖЕТ ИМЕТЬ ТАКОЙ ВИД 
# word = input()

# if word == 'Python' : 
#     print('DA')
# else : 
#     print('NET')    



# Задача 2.
# Напишите программу, которая определяет, состоит ли двузначное число, введенное с клавиатуры, из одинаковых цифр. 
# #Если состоит, то программа выводит «ДА», в противном случае программа выводит «НЕТ».

# num = int(input())

# last_digit = num % 10   # poslednee cifra chislo
# first_digit = num // 10 # pervoe cifra chislo

# if last_digit == first_digit : 
#     print('DA')
# else : 
#     print('NET')



# Задача 3. 
# Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел.

# num1, num2, num3 = int(input()), int(input()), int(input())

# counter = 0 # переменная счетчик
# if num1 % 2 == 0:
#     counter = counter + 1 # увеличиваем счетчик на 1
# if num2 % 2 == 0 :
#     counter = counter + 1 # увеличиваем счетчик на 1   
# if num3 % 2 == 0 : 
#     counter = counter + 1 # увеличиваем счетчик на 1

# print(counter)




# проверка правильности пароля

# right_pin = input()
# pin = input()

# if right_pin == pin : 
#      print('Пароль принят')
# else : 
#      print('Пароль не принят')    



# Проверка четное или нечетное число

# num = int(input())

# if num % 2 == 0 : 
#     print('chet')
# else : 
#     print('ne chet')    



# проверка возраста

# age = int(input())

# if age < 18 :
#     print('Доступ запрещен')
# else : 
#     print('Доступ разрешен')    



# программа что определяет наименьшее из двух чисел 

# num1 = int(input())
# num2 = int(input())

# if num1 < num2 :
#     print(num1)
# else : 
#     print(num2)




# программа что определяет являются ли 3 числа последовательными числами арифметической прогрессии 

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())

# if (num2 - num1) + num2 == num3 : 
#     print('YES')
# else :
#     print('NO')




# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение
# сумма первой и последней цифр равна разности второй и третьей цифр.

# abcd = int(input())

# d = abcd % 10
# c = (abcd // 10) % 10
# b = (abcd // 100) % 10
# a = abcd // 1000

# if a + d == b - c : 
#     print('ДА')
# else :
#     print('НЕТ')




# написать программу что считает сумму только положительных чисел

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())

# if num1 < 0 :
#      num1 = 0 
# if num2 < 0 :
#      num2 = 0
# if num3 < 0 :
#     num3 = 0 

# print(num1 + num2 + num3)




# написать программу что по выводит возрастную группу 

# age = int(input())

# if age <= 13 :
#     print('детство')
# if 14 <= age <= 24  :
#     print('молодость')
# if 25 <= age <= 59  :
#     print('зрелость')
# if age >= 60 :
#     print('старость')




# Напишите программу, которая определяет наименьшее из четырёх чисел.

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# if a > b : 
#     x = b
# else :
#     x = a
# if c > d :
#     y = d 
# else : 
#     y = c 

# if x < y :
#     print(x)
# else : 
#     print(y)




# Задача 1. Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 
# 3 (если все совпадают), 
# 2 (если два совпадает) или 
# 0 (если все числа различны). 

# Программа, решающая поставленную задачу, может иметь следующий вид:

# 1 СПОСОБ УСЛОВНЫЙ ВЛОЖЕННЫЙ ОПЕРАТОР 

# a, b, c = int(input()), int(input()), int(input())

# if a == b:
#     if b == c:
#         print(3)
#     else:
#         print(2)
# else:
#     if a == c:
#         print(2)
#     else:
#         if b == c:
#             print(2)
#         else:
#             print(0)


# 2 СПОСОБ ИСПОЛЬЗОВАНИЕ УСЛОВНОГО ОПЕРАТОРА

# a, b, c = int(input()), int(input()), int(input())

# if a == b == c:
#     print(3)
# elif a == b:
#     print(2)
# elif b == c:
#     print(2)
# elif a == c:
#     print(2)
# else:
#     print(0)


# 3 СПОСОБ ИСПОЛЬЗОВАНИЕ КАСКАДНОГО УСЛОВНОГО ОПЕРАТОРА И ЛОГИЧЕСКОГО ОПЕРАТОРА or

# a, b, c = int(input()), int(input()), int(input())

# if a == b == c:
#     print(3)
# elif a == b or b == c or a == c:
#     print(2)
# else:
#     print(0)


# angle = 89

# if angle < 90:
#     print('Меньше 90')
# elif angle > 180:
#     print('Больше 180')
# elif angle < 270:
#     print('Меньше 270')



# angle = 291
# if angle % 90 == 0:
#     if angle == 0:
#         print('Нулевой')
#     elif angle == 90:
#         print('Прямой')
#     elif angle == 180:
#         print('Развёрнутый')
# else:
#     if 0 < angle < 90:
#         print('Острый')
#     elif 90 < angle < 180:
#         print('Тупой')
#     elif 180 < angle < 270:
#         print('Выпуклый')
#     else:
#         print('Ни острый, ни тупой, ни выпуклый')




# ЗАДАЧА 1 ПРОГРАММА ЧТО ВЫВОДИТ ОТВЕТ НА ВОПРОС 

# z = int(input())
# f = int(input())

# if z > f:
#     print('NO')
# elif f > z:
#     print('YES')
# else:
#     print("Don't know")



# ЗАДАЧА 2 ПРОГРАММА ЧТО ОПРЕДЕЛЯЕТ ВИД ТРЕУГОЛЬНИКА 

# a = int(input())
# b = int(input())
# c = int(input())

# if a == b == c:
#     print('Равносторонний')
# elif (a == b and a != c ) or (a == c and a != b ) or (b == c and b != a) :
#     print('Равнобедренный')    
# elif a != b != c and a != c:
#     print('Разносторонний')



# ЗАДАЧА 3 ПРОГРАММА ЧТО НАХОДИТ СЕРЕДИННОЕ ЗНАЧЕНИЕ

# a = int(input())
# b = int(input())
# c = int(input())

# if a < b < c or a > b> c:
#     print(b)
# elif b < a < c or b > a > c:
#     print(a)
# else:
#     print(c)



# ЗАДАЧА 4 ПРОГРАММА ЧТО ВЫДАЕТ КОЛИЧЕСВТО ДНЕЙ В МЕСЯЦЕ

# month = int(input())

# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     print(31)
# elif month == 2:
#     print(28)
# else:
#     print(30)



# ЗАДАЧА 5 ПРОГРАММА ЧТО ОПЕРЕДЕЛЯЕТ ВЕСОВУЮ КАТЕГОРИЮ БОЙЦА 

# weight = int(input())

# if 60 > weight:
#     print('Легкий вес')
# elif 60 <= weight < 64:
#     print('Первый полусредний вес')
# elif 64 <= weight < 69:
#     print('Полусредний вес')



# ЗАДАЧА 6 ПРОГРАММА ЧТО ВЫПОЛНЯЕТ ТО ЧТО СЧИТАЛА СО СТРОКИ (ЮРЧИК ПОМОГ)

# num1 = int(input())
# num2 = int(input())
# txt = str(input()) # * + - / 

# if num2 == 0 and txt == '/':
#     print('На ноль делить нельзя!')
# else:
#     if txt == '*':
#         print(num1 * num2)
#     elif txt == '/':
#         print(num1 / num2)
#     elif txt == '+':
#         print(num1 + num2)  
#     elif txt == '-':
#         print(num1 - num2)

#     else:
#         print('Неверная операция')



# ЗАДАЧА 7 ПРОГРАММА ЧТО СЧИТЫВАЯ ДВА ЦВЕТА А ВЫВОДИТ НАЗВАНИЕ ТРЕТЬЕГО (ГПТ ПОМОГ ПОНЯТЬ ГДЕ ОШИБКА)

# a = input()
# b = input()
 
# if a == b:   # Я ЕБЛАН НЕ ТАК ПРОЧИТАЛ УСЛОВИЕ И ПОЭТОМУ У МЕНЯ В ПРИНТЕ БЫЛО НЕ а , А ОШИБКА ЦВЕТА
#     print(a) # А ВСЕ ОСТАЛЬНОЕ БЫЛО ПРАВИЛЬНО 
# elif a != 'красный' and a != 'синий' and a != 'желтый':
#     print('ошибка цвета')
# elif b != 'красный' and b != 'синий' and b != 'желтый': 
#     print('ошибка цвета')
# elif (a == 'красный' and b == 'синий') or (a == 'синий' and b == 'красный'):
#     print('фиолетовый')
# elif (a == 'красный' and b == 'желтый') or (b == 'красный' and a == 'желтый'):
#     print('оранжевый')
# elif (a == 'синий' and b == 'желтый') or (b == 'синий' and a =='желтый' ):
#     print('зеленый') 



# ЗАДАЧА 8 написать программу определяющую цвет кармана на колесе лудки (тоже помогал гпт)

# n = int(input())


# if n < 0 or n > 36:
#     print('ошибка ввода')
# elif n == 0:
#     print('зеленый')
# elif (1 <= n <= 10) or (19 <= n <= 28):
#     if n % 2 != 0: 
#         print('красный')
#     else:  
#         print('черный')
# elif (11 <= n <= 18) or (29 <= n <= 36):
#     if n % 2 != 0: 
#         print('черный')
#     else:
#         print('красный')




# ЗАДАЧА 9 ПРОГРАММА ЧТО НАХОДИТ ТОЧКИ ПЕРЕСЕЧЕНИЯ 

# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())

# if b1 < a2 or b2 < a1:
#     print('пустое множество')
# elif b1 == a2:
#     print(b1)
# elif a1 == b2:
#     print(a1)
# elif a1 == a2 and b1 == b2:
#     print(a1, b1)
# elif a1 <= a2 and b1 <= b2:
#     print(a2, b1)
# elif a2 <= a1 and b2 <= b1:
#     print(a1, b2)
# elif a1 < a2 and b2 <= b1:
#     print(a2, b2)
# elif a2 < a1 and b1 <= b2:
#     print(a1, b1)






















































































































