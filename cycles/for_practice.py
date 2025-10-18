# ПРОГРАММА ЧТО ВЫВОДИТ ТЕКСТ 10 РАЗ

# for i in range(10):
#     print('Python is awesome!')




# ПРОГРАММА ЧТО ВЫВОДИТ ТЕКСТ 

# for i in range(6):
#     print('AAA')
# for i in range(5):
#     print('BBBB')
# print('E')
# for i in range(9):
#     print('TTTTT')
# print('G')





# a = input()
# for i in range(int(input())):
#     print(a)





# n = int(input())

# for i in range(n):
#     print('*' * 19)




# for i in range(4):
#     print(i, end='*')


# for i in range(4):
#     j = i + 1
#     print(i, j)



# a = input()
# for i in range(10):
#     print(i , a)




# n = int(input())

# for i in range(n + 1):
#     print('Квадрат числа', i, 'равен', i ** 2)




# n = int(input())
# for i in range(n):
#     print('*' * (n - i))




# m = int(input()) # СТАРТОВОЕ КОЛИ-ВО ОРГАНИЗМОВ
# p = int(input()) # СРЕДНЕСУТОЧНОЕ УВЕЛИЧЕНИЕ В %
# n = int(input()) # КОЛИЧЕСТВО ДНЕЙ 

# for i in range(n):
#     print(i + 1,m * (p / 100 + 1) ** i)




# for i in range(4, 8, 2):
#     print(i)




# for i in range(1, 10, 3):
#     print(i, sep='?')




# m = int(input())
# n = int(input())
# for i in range(m, n + 1):
#     print(i)





# m = int(input())
# n = int(input()) 
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# elif m > n:
#     for i in range(m, n - 1, -1):
#         print(i)
# elif m == n:
#     print(m)





# m = int(input())
# n = int(input()) 

# if m % 2 != 0:
#     for i in range(m,n - 1, -2):
#         print(i)
# elif m % 2 == 0:
#     for i in range(m, n, -2):
#         print(i - 1)




# m = int(input())
# n = int(input()) 

# for i in range(m, n + 1):
#     if i % 10 == 9:
#         print(i)
#     elif i % 17 == 0:
#         print(i)
#     elif (i % 3 + i % 5) == 0:
#         print(i)




# n = int(input())

# for i in range(10):
#     print(n, 'x', i + 1, '=', n * (i +1))




# total = 0
# for i in range(1, 6):
#     total += i
# print(total)


# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')




# ПРОГРАММА ЧТО ИЩЕТ КУБЫ ОКАНЧИВАЮЩИЕСЯ НА 4 ИЛИ 9

# a = int(input())
# b = int(input())
# counter = 0
# for i in range(a, b + 1):
#     if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
#         counter = counter + 1
# print(counter)




# ПРОГРАММА ЧТО СЧИТАЕТ СУММУ ВВЕДЕННЫХ ЧИСЕЛ 

# total = 0
# n = int(input())
# for i in range(n):
#     num = int(input())
#     total += num
# print(total)




# ПРОГРАММА ЧТО НАХОДИТ АСИМПТОТИЧЕСКОЕ ПРИБЛИЖЕНИЕ 
# from math import log


# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     total += 1 / i
# print(total - log(n))




# ПРОГРАММА ЧТО СЧИТАЕТ СУММУ ЧИСЕЛ КВАДРАТ КОТОРЫХ ЗАКАНЧИВАЕТСЯ НА 2, 5, 8

# n = int(input())
# counter = 0
# for i in range(n):
#     if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
#         counter += i
# print(counter)




# ПРОГРАММА ЧТО НАХОДИТ ФАКТОРИАЛ ЧИСЛА

# from math import factorial


# n = int(input())
# print(factorial(n))




# ПРОГРАММА ЧТО СЧИТАЕТ ПРОИЗВЕДЕНИЕ ЧИСЕЛ КОТОРЫЕ ОТЛИЧНЫЕ ОТ НУЛЯ

# total = 1
# for i in range(10):
#     num = int(input())
#     if num != 0:
#         total *= num
# print(total)




# ПРОГРАММА ЧТО СЧИТАЕТ СУММУ ВСЕХ ДЕЛИТЕЛЕЙ ЧИСЛА

# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         total += i
# print(total)




# ПРОГРАММА ЧТО ОПРЕДЕЛЯЕТ ЯВЛЯЮТСЯ ЛИ ВСЕ ЧИСЛА ЧЕТНЫМИ  

# total = 0
# for i in range(10):
#     num = int(input())
#     if num % 2 == 0:
#         total += 1
# if total == 10:
#     print('YES')
# else:
#     print('NO')




# ПРОГРАММА ЧТО НАХОДИТ ЗНАКОЧЕРЕДУЮЩУЮСЯ СУММУ 

# n = int(input())
# total = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         total -= i
#     else:
#         total += i
# print(total)




# ПРОГРАММА ЧТО ВЫВОДИТ НАИБОЛЬШЕЕ ЧИСЛО 

# n = int(input())
# max1 = 0
# max2 = 0

# for i in range(1, n + 1):
#     num = int(input())
# if num > max1:
#     max2 = max1
#     max1 = num
# elif num > max2:
#     max2 = num
# print(max1)
# print(max2)




# n = int(input())
# f1 = 0 
# f2 = 1 

# for _ in range(0, n):
#     f1, f2 = f2, f1 + f2
#     print(a, end = " ")










