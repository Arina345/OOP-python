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


class Human:
    print("Инструкция выполняется")


# Создание атрибута класса аналогично созданию обычной переменной
# Методы начинаются с def


class Human:
    n = 5

    def adder(v):
        return v + Human.n


print(Human.n)  # Вывод 5
print(Human.adder(4))  # Вывод 9


# Если это атрибут класса,то <Имя класса>.<Имя атрибута>
# Если это атрибут- метод ,то <Имя класса>.<Имя метода>([<Параметры>])


# self - это ссылка на экземпляр класса


class Myclass:
    x = 10

    def __init__(self):
        self.y = 20


c1 = Myclass()
c2 = Myclass()

print(c1.x, c2.x, sep="\t")
Myclass.x = 88  # изменяем атрибут объекта класса
print(c1.x, c2.x, sep="\t")
c1.y = 88  # создаем атрибут экземпляра
print(c1.y, c2.y, sep="\t")

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


class Class1:
    def __init__(self):
        print("Конструктор базового класса")

    def func1(self):
        print("Метод func1 () класса Class1 ")


class Class2(Class1):  # Указываем от какого класса будет наследоваться
    def __init__(self):
        super().__init__()  # Вызываем конструктор базового класса
        print("Конструктор производного класса")
        Class1.__init__(self)  # Вызываем конструктор базового класса
        super(Class1, self).__init__()  # Вызываем конструктор базового класса

    def func1(self):
        print("Метод func1() класса Class2")
        Class1.func1(self)


c = Class2()  # Создаем экземпляр класса Class2
c.func1()  # Вызываем метод func1()
