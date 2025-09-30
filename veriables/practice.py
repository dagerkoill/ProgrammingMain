# flat_num = 24

# entrance_num = (flat_num - 1) // 20 + 1   # вычисляем подъезд
# floor_num = (flat_num - 1) % 20 // 4 + 1  # вычисляем этаж 
# print(entrance_num) # подъезд
# print(floor_num)    # этаж


# s = 0
# k = 30
# d = k - 5
# k = 2 * d
# s = k - 100

# print(s)


# x = 3 
# y = 4 
# z = x + y # z = 3 + 4 = 7
# z = z + 1 # z = 7 + 1 = 8
# x = y # ни на что не влияет
# y = 5
# x = z + y + 7 # x = 8 + 5 + 7 = 20

# print(x)



# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())

# print( (num1 + num2 + num3 + num4) * 3)



# a = int(input())
# b = int(input())

# print(3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41)




# a = int(input())

# print('Следующее за числом', a, 'число:', a + 1)
# print('Для числа', a, 'предыдущее число:', a - 1)



# a = int(input())
# V = a ** 3
# S = 6 * a ** 2 

# print('Объем =', V)
# print('Площадь полной поверхности =', S)



# a = int(input())
# b = int(input())
# c = a + b
# d = a - b
# e = a * b
# print(a, '+', b, '=', c)
# print(a, '-', b, '=', d)
# print(a, '*', b, '=', e)



# a1 = int(input())
# d = int(input())
# n = int(input())
# an = a1 + d * (n - 1)

# print(an)



# x = int(input())

# print(x, 2 * x, 3 * x, 4 * x, 5 * x, sep = '---')



# b1 = int(input())
# q = int(input())
# n = int(input())
# bn = b1 * q ** (n-1)

# print(bn)



# cm = int(input())
# m = cm // 100

# print(m)

# дают кол-во школьников и мандаринов . Вывести сколько каждому мандаринов, и сколько останется в корзине

# n = int(input()) # школьники 
# k = int(input()) # мандарины
# print(k // n)
# print(k % n)


# дают население планеты , если не четное то число должно округлится в большую сторону

# naselenie = int(input()) + 1
# print(naselenie // 2)

# ДРУГОЙ ВАРИАНТ РЕШЕНИЯ
# n = int(input())
# print(n // 2 + n % 2) 



#Дают минуты , нужно перевести в часы и минуты + вывести все это с текстом 

# minute = int(input())
# hour = minute // 60 
# print(minute, 'мин - это', hour, 'час', minute % 60, 'минут.')



# Дают номер койки в купе , вывечти в каком купе она находится

# bed = int(input())

# coupe = (bed - 1) // 4 + 1
# print(coupe)


# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100

# print(digit1, digit2, digit3, sep = ',')


# Вывести сумму и произведение цифр из числа 

# num = int(input())
# dig3 = num % 10
# dig2 = (num // 10) % 10
# dig1 = num // 100
# summery = dig1 + dig2 + dig3
# product = dig1 * dig2 * dig3
# print('Сумма цифр =', summery )
# print('Произведение цифр =', product)




# Вывести 6 разных чисел из 3 разных цифр 

# abc = int(input())
# c = abc % 10
# b = (abc // 10) % 10
# a = abc // 100
# print(abc)
# print(a * 100 + c * 10 + b)
# print(b * 100 + a * 10 + c)
# print(b * 100 + c * 10 + a)
# print(c * 100 + a * 10 + b)
# print(c * 100 + b * 10 + a)

# Так тоже можно 
# a,b,c = input()
# print(a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a, sep='\n')



# Напишите программу для нахождения цифр четырёхзначного числа.

# abcd = int(input())
# d = abcd % 10
# c = (abcd // 10) % 10
# b = (abcd // 100) % 10
# a = abcd // 1000
# print(a, b, c, d, sep = '\n')


