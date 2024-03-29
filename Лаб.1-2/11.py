# Задача 11

# Написать программу, которая выводит на экран вопрос и 5 вариантов ответа.
# Пользователь должен ввести с клавиатуры номер выбранного варианта ответа.
# Программа должна проверить его ответ и сообщить результат.

# Вопрос:Аргументы функции, которые передаются без указания имен, называются
# Первый вариант ответа: особенные
# Второй вариант ответа: позиционными
# Третий вариант ответа: необзятельными
# Четвертый вариант ответа: обычными
# Пятый вариант ответа: именнованными

# Правильный ответ: позиционными

v = "Аргументы функции, которые передаются без указания имен, называются:"

answer = {
    1: "особенные",
    2: "позиционными",
    3: "необзятельными",
    4: "обычными",
    5: "именнованными",
}

# Правильный ответ
correct = 2

print("Вопрос:", v)
print()

for key, value in answer.items():
    print(key, ":", value)

user = int(input("Введите номер ответа :"))

if user == correct:
    print("Ответ правильный")
else:
    print("Ответ неправильный")
