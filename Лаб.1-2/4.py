# Задача 4

# Написать программу, которая запрашивает у пользователя положительное целое число.
# Программа должна вывести на экран квадраты чисел от 1 до введенного числа.
# Дополнительно необходимо проверить введенные пользователем данные.

number = int(input())

if number < 0:
    print("Введено отрицательное число")

else:
    for i in range(1, number):
        print(i**2)
