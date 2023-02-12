# Задача 9.
# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1.
# Решить задачу используя цикл while.
# Input: 5
# Output: 120

# # v.1
# factorial = 1
# n = int(input('Введите число: '))
# for i in range(1, n + 1):
#     factorial *= i
#     # print(i)
#     # print(factorial)
# print('Факториал числа', n, 'равен', factorial)

# # v.2
# num = int(input('Введите число: '))
# factorial = 1
# while num > 1:
#     factorial *= num
#     num -= 1
# print(f'Факториал равен {factorial}')

# v.3
num = int(input('Введите число: '))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f'Факториал равен {factorial}')