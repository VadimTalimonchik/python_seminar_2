# Задача 11.
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# # Вариант 1
# fib1 = 0
# fib2 = 1

# i = 1
# n = input('Номер элемента ряда Фибоначчи: ')
# n = int(n)
# fib_sum = 0
# while fib_sum < n:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1

# if fib_sum == n:
#     print('Значение этого элемента: ', i)
# else:
#     print(-1)

# -------------------------
# # Вариант 2
# x = 0
# x1 = 1
# x2 = 0
# i = 0

# n = int(input('Введите число: '))
# while x <= n:
#     x = x1 + x2
#     x1, x2 = x, x1
#     i += 1

# if(n == x2):
#     print(i)
# else:
#     print(-1)

# ---------------------
# Вариант 3 ???
n = int(input('Введите число: '))
n0 = 0
n1 = 0
n2 = 1
i = 2
while n0 < n:
    n0 = n1 + n2
    n1 = n2
    n2 = n0
    i += 1
    if n0 > n:
        i = 0
        if i != 0:
            print(i)
        else:
            print(-1)
            
# вариант 3 надо доработать