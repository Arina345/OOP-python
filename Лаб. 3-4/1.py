# Создать классы Cat, Dog и Chicken.
# Для каждого класса создать метод get_sound и атрибут name.

# При обращении к атрибуту name должна возвращаться строка, содержащая кличку питомца

# При вызове метода get_sound в зависимости от класса в консоль должен
# выводиться следующий текст:

# «мяю» - для Cat,
# «гав-гав» - для Dog,
# «чик-чик» - для Chicken.

# Создайте список Animals, содержащий не менее 3х экземпляров каждого класса.
# Затем создайте цикл, в котором у каждого элемента списка будет выведен на экран атрибут name и вызван метод get_sound.

# Для каждого класса создать метод add_friend, при вызове данного метода, ему должен аргументом передаться любой объект.
# Переданный объект должен расширить список «друзей» экземпляра класса, являющимся атрибутом friends.


# ДОПОЛНИТЕЛЬНО

# В методе add_friend должна осуществляться проверка добавляемого объекта.
# Каждый класс может иметь в «друзьях» не более 2х типов объектов и не более пяти экземпляров в общей сумме.
# То есть, для класса должны быть определены два типа объектов, которых можно добавить в список, и суммарно в этом списке может быть не более пяти элементов.

# Реализовать метод «список друзей» для каждого класса: на экран выводится имя каждого элемента списка или сообщение о пустоте списка.


class Cat:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def get_sound(self):
        return "мяу"

    def add_friend(self, friend):
        self.friends.append(friend)
        if not isinstance(friend, (Cat, Dog)) and len(self.friends) >= 5:
            return []
        else:
            for f in self.friends:
                print(f)


class Dog:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def get_sound(self):
        return "гав-гав"

    def add_friend(self, friend):
        self.friends.append(friend)

        # s = len(set(type(i) for i in self.friends))
        # print(s)


class Chicken:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def get_sound(self):
        return "чик-чик"

    def add_friend(self, friend):
        self.friends.append(friend)


# Экземпляры классов Cat, Dog, Chicken
cat = Cat("Персик")
dog = Dog("Сеня")
chicken = Chicken("Федор")

print(cat.name, cat.get_sound(), sep="\t")

print(dog.name, dog.get_sound(), sep="\t")

print(chicken.name, chicken.get_sound(), sep="\t")

print("--------------------------------------------------------")

# --------------------------------------------------------------------------------------------------------------------------------

animals_names = [
    "Барсик",
    "Рей",
    "Федор",
    "Вася",
    "Арчи",
    "Петя",
    "Кеша",
    "Коля",
    "Женя",
]

animals = [(Cat, Dog, Chicken)[i % 3](animals_names[i]) for i in range(9)]


for animal in animals:
    print(
        "Кличка:{}".format(animal.name), "Звук:{}".format(animal.get_sound()), sep="\t"
    )
    print()


# --------------------------------------------------------------------------------------------------------------------------------
print("--------------------------------------------------------")


# Добавление друзей

cat.add_friend("Мурзик")
cat.add_friend(dog.name)
dog.add_friend(cat.name)
# print(cat.friends)
# print(dog.friends)
