# Задача 9.
# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1.
# Решить задачу используя цикл while.
# Input: 5
# Output: 120

factorial = 1
n = int(input('Введите число: '))
for i in range(1, n + 1):
    factorial *= i
    # print(i)
    # print(factorial)
print('Факториал числа', n, 'равен', factorial)