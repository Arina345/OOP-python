# students = [{"name": "Igor", "age": 22}, {"name": "Ivan", "age": 23}]

# print(*[s["name"] for s in students], sep="\n")


# class Students:
#     def __init__(self, name, age):
#         print(name)
#         self.name = name
#         self.age = age

#     def info_student(self):
#         return f"Имя: {self.name} Возраст: {self.age}\t"


# точка входа
# if __name__ == "__main__":
# Конструкция if name == 'main' Эта конструкция позволяет разработчикам определять, какие действия должны выполняться при запуске файла, и какие - при импорте.


# Экземпляр класса
# a1 = Students("Mixa", 22)

# animal_names = ["Иван", "Петя", "Муся", "Стрелка"]

# animals = [(Cat, Dog)[i % 2](animal_names[i]) for i in range(4)]


# a1 = Cat(name="Мася")
# a2 = Dog(name="Сеня")

# print(a1.get_sound(), a2.get_sound(), sep="\n")

# print(animals)

# for a in animals:
#     # вызов метода
#     a.get_sound()


# Функция super () в Python позволяет наследовать базовые классы (они же суперклассы или родительские классы) без необходимости явно ссылаться на базовый класс.
# super позволяет вызывать повдение родительского класса

# Основное преимущество концепции наследования в программировании - это вынос одинакового кода из разных классов в один родительский класс

# Инкапсуляция - сокрытие данных,т.е. невозможность напрямую получить доступ к внутренней структуре объекта,т.к. это не безопасно.
# Второй смысл инкапсуляции - объединение описания свойств объектов и их поведения в единое целое,т.е. в класс

# В ООП под полиморфизмом понимается следующее.Объекты разных классов с разной внутренней реализацией, т.е. программный кодом,могут иметь "Одинаковые методы".
# На самом деле у методов совпадают только имена,а вложенный код в них различен (то,что они делают)


# Класс описывается с помощью ключевого слова class


# class Human: ...


# # где Human - название класса


# class Human:
#     print("Инструкция выполняется")


# # Создание атрибута класса аналогично созданию обычной переменной
# # Методы начинаются с def


# class Human:
#     n = 5

#     def adder(v):
#         return v + Human.n


# print(Human.n)  # Вывод 5
# print(Human.adder(4))  # Вывод 9


# Если это атрибут класса,то <Имя класса>.<Имя атрибута>
# Если это атрибут- метод ,то <Имя класса>.<Имя метода>([<Параметры>])


# self - это ссылка на экземпляр класса


# class Myclass:
#     x = 10

#     def __init__(self):
#         self.y = 20


# c1 = Myclass()
# c2 = Myclass()

# print(c1.x, c2.x, sep="\t")
# Myclass.x = 88  # изменяем атрибут объекта класса
# print(c1.x, c2.x, sep="\t")
# c1.y = 88  # создаем атрибут экземпляра
# print(c1.y, c2.y, sep="\t")

# Изменение атрибута объекта класса х затронуло значение в обоих экземплярах класса.
# Аналогичная операция с атрибутом у изменяет знаечние только в екземпляре с1


# # Наследование

# class Human:
#     def __init__(self, name, sname, mname, age):
#         self.firstname = name
#         self.secondname = sname
#         self.middlename = mname
#         self.age = age
#         print(f"{self.firstname} created")

#     def increase_age(self, val=1):
#         self.age += val
#         print(f"{self.firstname} стал старее на {val}")
#         print(f"Теперь его возраст {self.age}")


# class Student(Human):
#     def __init__(self, name, sname, mname, age, zach):
#         self.zach = zach
#         s = super()
#         s.__init__(name, sname, mname, age)


# # Полиморфизм
# class Cat:
#     def get_sound(self):
#         print("Мяу")


# class Dog:
#     def get_sound(self):
#         print("Гав")


# class Bird:
#     def get_sound(self):
#         print("Чирик")


# class Class1:
#     def __init__(self):
#         print("Конструктор базового класса")

#     def func1(self):
#         print("Метод func1 () класса Class1 ")


# class Class2(Class1):  # Указываем от какого класса будет наследоваться
#     def __init__(self):
#         super().__init__()  # Вызываем конструктор базового класса
#         print("Конструктор производного класса")
#         Class1.__init__(self)  # Вызываем конструктор базового класса
#         super(Class1, self).__init__()  # Вызываем конструктор базового класса

#     def func1(self):
#         print("Метод func1() класса Class2")
#         Class1.func1(self)


# c = Class2()  # Создаем экземпляр класса Class2
# c.func1()  # Вызываем метод func1()


# class Cat:
#     def __init__(self, name):
#         self.name = name
#         self.friend = []

#     def get_sound(self):
#         return "мяу"

#     def add_friend(self, friends):
#         if isinstance(friends, (Cat, str)) == True:
#             self.friend.append(friends)
#         else:
#             raise ValueError("Объект такого типа нельзя добавить")
#         if len(self.friend) > 5:
#             raise ValueError("В списке больше 5 элементов")


# class Dog:
#     def __init__(self, name):
#         self.name = name
#         self.friend = []

#     def get_sound(self):
#         return "гав-гав"

#     def add_friend(self, friends):
#         self.friend.append(friends)


# cat = Cat("Мурзик")
# cat.add_friend(Cat("Пашка"))

# cat_friend = ["Лилия", "Гоша", Cat("Мишка")]

# for f in cat_friend:
#     cat.add_friend(f)
#     print(type(f))
# print((cat.friend))

# cat.add_friend(Dog("Миша"))

# print(cat.friend)


# print(isinstance("Рома", (Cat, str)))


# Создать класс Human. При создании экземпляра класса ему должны передаться в формате строки обязательные параметры: фамилия, имя, отчество.

# Также класс должен получить необязательные параметры возраст и пол.

# Возраст по умолчанию равен нулю. Пол указывается строкой «М» или «Ж», значение по умолчанию любое из 2х вариантов.

# В классе Human реализовать 2 метода:
# 1) get_fio – возвращает строку в формате «Фамилия И. О.»
# 2) get_full_info – возвращает строку в формате:

# Фамилия: {…}
# Имя: {…}
# Отчество: {…}
# Пол: {…}
# Возраст: {…}
# - где {…} соответствующее значение атрибута объекта. Переносы строк – обязательны.


class Human:
    def __init__(self, name, surname, middlname, age=0, sex="«М» или «Ж»"):
        self.name = name
        self.surname = surname
        self.middlname = middlname
        self.age = age
        self.sex = sex

    def get_fio(self):
        return "{0} {1}.{2}.".format(self.surname, self.name[0], self.middlname[0])

    def get_full_info(self):
        print(
            f"Фамилия: {self.surname} \nИмя: {self.name} \nОтчество: {self.middlname} \nПол: {self.sex} \nВозраст: {self.age}"
        )


# Экземпляр класса
person = Human("Арина", "Крикунова", "Васильевна", 20, "Ж")

print("----------------------get_full_info()----------------------------------")
print(person.get_full_info())
print("----------------------get_fio()----------------------------------------")
print(person.get_fio())

print("----------------------class Student------------------------------------")
# Создать класс Student, который наследуется от класса Human.
# Переопределить в данном классе метод __init__ таким образом, чтобы он
# принимал обязательный параметр номера группы в формате строки.


# Переопределить метод get_full_info таким образом, чтобы к выводу добавилась строка «Группа: {…}».


class Student(Human):
    def __init__(self, name, surname, middlname, age, sex, ng):
        super().__init__(name, surname, middlname, age, sex)
        self.ng = ng

    def get_full_info(self):
        # вызываем метод родительского класса
        super().get_full_info()
        # Добавляем свое поведение
        return f"Группа: {self.ng}"


p = Student("Арина", "Крикунова", "Васильевна", 20, "Ж", "ИСТБ-31")

print(p.get_full_info())

# person_modern = Student()

# person_modern.get_full_info()


# class A:
#     def __init__(self, x):
#         print("Инициализация в A")
#         self.x = x

#     def sum(self):
#         return self.x + 1


# class B(A):
#     def __init__(self, x, y):
#         print("Инициализация в B")
#         super().__init__(x)
#         self.y = y

#     def mun(self):
#         return self.y * self.x


# b = B(42, 3.14)
# print(b.sum())
# print(b.mun())


# about = [
#     {
#         "surname": self.surname,
#         "name": self.name,
#         "middlname": self.middlname,
#         "sex": self.sex,
#         "age": self.age,
#     }
# ]


# return f"Фамилия: {about[0]['surname']} \nИмя: {about[0]['name']} \nОтчество: {about[0]['middlname']} \nПол: {about[0]['sex']} \nВозраст: {about[0]['age']}"
# class A:
#     def some_method(self):
#         print("some_method A")


# class B(A):
#     def some_method(self):
#         # вызываем метод родительского класса
#         super().some_method()
#         # Добавляем свое поведение
#         print("some_method B")


# x = B()
# print(x.some_method())
