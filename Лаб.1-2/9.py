# Задача 9

# Написать функцию, которая возвращает случайную дату в следующем формате «дд-мм-гггг».

import datetime, random

y = random.randint(1995, 2004)  # год
m = random.randint(1, 12)  # месяц
d = random.randint(1, 31)  # день


def date(day, month, year):
    return datetime.date(year, month, day).strftime("%d-%m-%Y")


res = date(day=d, month=m, year=y)

print(res)
