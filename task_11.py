# Задача 11.
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# fib1 = 0
# fib2 = 1

# i = 1
# n = input('Номер элемента ряда Фибоначчи: ')
# n = int(n)
# fib_sum = 0
# while fib_sum <= n:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1

#     if fib_sum == n:
#         print('Значение этого элемента: ', i)
#     else:
#         print(-1)

# -------------------------
# # Вариант 2
# x = 0
# x1 = 1
# x2 = 1
# i = 3

# n = int(input('Введите число: '))
# while x <= n:
#     x = x1 + x2
#     x, x2 = x, x1
#     i += 1

# if(n == x2):
#     print(i)
# else:
#     print(-1)

# ---------------------
print("Введите число n:")
num = int(input())

fib0 = 0
fib1 = 1
fib2 = 1
i = 3
output = -1
while fib2 <= num:
    if fib2 == num:
        output = i
    fib2 = fib0 + fib1
    fib1 = fib2
    fib0 = fib1
    # print(i, ":", fib2) # Проверка правильности решения
    i += 1

print("Input:", num)
print("Output:", i)


# требуется доработка