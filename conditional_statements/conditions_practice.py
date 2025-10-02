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








