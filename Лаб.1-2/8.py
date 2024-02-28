# Задача 8

# Написать программу, которая запрашивает у пользователя целое число больше 5.
# Так же программа должна сгенерировать число от 0 до 5.
# Оба числа должны быть переданы в функцию, созданную в задаче №7.
# На экран должен быть выведен результат работы функции.
# Дополнительно необходимо проверить введенное пользователем число

import random

number_one = int(input())

number_two = random.randrange(0, 5)
# print(number_two)


def multiplication(a, b):
    return a * b


if number_one > 5 and number_one != 5:
    res = multiplication(number_one, number_two)
    print(res)
else:
    print("Введенное число меньше или равно 5")
