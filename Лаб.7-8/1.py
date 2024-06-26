# Создайте класс, который при инициализации принимает параметр «путь
# до файла». Если файл не существует (проверка с помощью модуля os), то его
# необходимо создать при инициализации объекта данного класса.

# В атрибут words должен быть помещен список всех слов из текста.

# У класса должны быть следующие методы:
# 1) delete_word – должен удалить слово, которое было передано в вызов данного метода.
# 2) update_source – сохраняет все слова обратно в файл

import os


class File:
    words = []

    def __init__(self, path):
        self.p = path

    def path(self):
        "Если файла нет,то создаем его"
        if os.path.isfile(self.p) == False:
            file = open(self.p, "x", encoding="utf-8")
            return file
        # Иначе выводим
        else:
            return "Файл уже создан"

    def delete_word(self, word):
        "Слово,которое нужно удалить"
        self.word = word
        "Если это слово есть в списке words, то удаляем"
        if self.word in self.words:
            self.words.remove(self.word)
            return f"Слово -{self.word}- было  успешно удалено из списка {self.words}"
        else:
            return f"Слово -{self.word}- не было удалено,так как его нет в списке слов {self.words}"

    def update_source(self):
        with open(self.p, "w+", encoding="utf-8") as text_file:
            text_file.write(" ".join(self.words))
            text_file.seek(0)
            return text_file.read()

    # -----------------------------------ДОПОЛНИТЕЛЬНО--------------------------------------
    # Добавить метод delete_char, который удаляет переданный символ из всех слов списка words.
    def delete_char(self, symbol):
        self.symbol = symbol
        with open(self.p, "r+", encoding="utf-8") as text_file:
            return text_file.read().replace(self.symbol, "")


# file = File("C:/Users/Арина Крикунова/Downloads/file.txt")
file = File("file.txt")

print(file.path())

with open(file.p, "w+", encoding="utf-8") as text_file:
    text_file.write(
        "open возвращает дескриптор файла, полученный Python-приложением от вашей операционной системы."
    )
    text_file.seek(0)
    file.words = [el for el in text_file.read().split(" ")]
    text_file.close()

print(file.delete_word("от"))
print(file.update_source())
print()
print(file.delete_char("о"))

# print(os.path.isfile("C:/Users/Арина Крикунова/Downloads/file.txt"))
