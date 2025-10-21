# a = input()
# while a != 'КОНЕЦ':
#     print(a)
#     a = input()




# ПРОГРАММА ЧТО СЧИТЫВАЕТ ТЕКСТ И ВЫВОДИТ ЕГО ДО СЛОВА КОНЕЦ ИЛИ конец
# a = input()

# while a != 'КОНЕЦ' and a != 'конец':
#     print(a)
#     a = input()




# ПРОГРАММА ЧТО СЧИТЫВАЕТ ТЕКСТ И ВЫВОДИ КОЛИЧЕСТВО СЛОВ ДО СТОП СЛОВА

# a = input()
# total = 0

# while a != 'стоп' and a != 'хватит' and a != 'достаточно':
#     total = total + 1 
#     a = input()
# print(total)




# a = int(input())

# while a % 7 == 0:
#     print(a)
#     a = int(input())
   



# num = int(input())
# total = 0

# while num >= 0:
#     total += num
#     num = int(input())

# print(total)




# num = int(input())
# total = 0

# while num > 0 and num < 6:
#     if num == 5:
#         total += 1
#     num = int(input())
# print(total)




# num = int(input())
# counter = 0

# while num >= 25:
#     counter += 1
#     num -= 25
# while num >= 10:
#     counter += 1
#     num -= 10
# while num >= 5:
#     counter += 1
#     num -= 5
# while num >= 1:
#     counter += 1
#     num -= 1

# print(counter)




# num = int(input())

# while num != 0:
#     last_digit = num % 10 
#     print(last_digit)
#     num = num // 10




# num = int(input())

# while num != 0:
#     last_digit = num % 10 
#     print(last_digit, end = '')
#     num = num // 10




# num = int(input())

# print('Максимальная цифра равна', max(str(num)))
# print('Минимальная цифра равна', min(str(num)))
# ПРИМЕР НУБА ОМЕЖКИ (из комментариев)


# ПРИМЕР АЛЬФАЧА(МЕНЯ) КОТОРЫЙ СИДЕЛ НАД ЭТИМ КОДОМ 30 МИНУТ 
# n = int(input())
# max_digit = 0 
# min_digit = 9 

# while n > 0:
#     digit = n % 10 
#     if digit > max_digit:
#         max_digit = digit
#     if digit < min_digit:
#         min_digit = digit
#     n = n // 10  

# print('Максимальная цифра равна', max_digit)
# print('Минимальная цифра равна', min_digit)




# num = int(input())
# total = 0   # summa
# counter = 0  # kol-vo
# product = 1   # proizvedenie
# last_digit = num % 10

# while num != 0:
#     first_digit = num % 10
#     total += first_digit
#     counter += 1
#     product *= first_digit
#     num = num // 10

# print(total, counter, product, total / counter, first_digit, first_digit + last_digit, sep = '\n')




# num = int(input())

# while num >= 10:
#     last_digit = num % 10
#     num = num // 10
# print(last_digit)




# num = int(input())

# if max(str(num)) == min(str(num)):
#     print('YES')
# else:
#     print('NO')



# num = int(input())
# flag = False
# count = 0 

# while num != 0:
#     last_digit = num % 10
#     if last_digit >= count:
#         flag = True
#         count = last_digit
#     else:
#         flag = False
#         break 
#     num = num // 10
# if flag == True:
#     print('YES')
# else:
#     print('NO')




# n = int(input())
# max_digit = -1  

# while n > 0:
#     digit = n % 10 
#     if digit % 3 == 0 and digit > max_digit:
#         max_digit = digit
#     n = n // 10  

# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)




# total = 0
# mx = -10**6 - 1
# flag = False

# for i in range(10):
#     num = int(input())
#     if num < 0:
#         total += num
#         if not flag or num > mx:
#             mx = num
#         flag = True

# if flag:
#     print(total)
#     print(mx)
# else:
#     print('NO')












































