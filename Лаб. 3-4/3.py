# доступные методы
# print(dir(c))

# Создайте класс Triangle (треугольник).
# Атрибуты, хранящие величину длины сторон треугольника, не должны быть доступны для чтения вне класса.

# При создании экземпляра класса в метод __init__ должны передаваться
# величины, соответствующие длинам сторон треугольника.

# Проверку устанавливаемых величин в данном методе делать не обязательно.


from typing import Any


class Triangle:
    # protected_attrs = "__one"
    # __one: int

    def __init__(self, lengthone, lengthtwo, lengthtree):
        self.__one = lengthone
        self.__two = lengthtwo
        self.__three = lengthtree

    # Создайте отдельный метод на изменение каждого скрытого атрибута с
    # проверкой присваемого значения на соответствие правилу треугольника:
    # длина одной стороны не должна превышать сумму длин остальных сторон.

    def triangle_rule(self):
        if self.__one > self.__two + self.__three:
            raise AttributeError(
                f"Не выполянется правило треуголника. Измените первое значение {self.__one}!"
            )

        elif self.__two > self.__one + self.__three:
            raise AttributeError(
                f"Не выполянется правило треуголника. Измените второе значение {self.__two}!"
            )
        elif self.__three > self.__one + self.__two:
            raise AttributeError(
                f"Не выполянется правило треуголника. Измените третье значение {self.__three}!"
            )

    # Создайте метод get_perimetr, который возвращает длину периметра.
    def get_perimetr(self):
        self.triangle_rule()
        return self.__one + self.__three + self.__two

    # ----------------------ДОПОЛНИТЕЛЬНО------------------------------------

    # Для запрета смены величины атрибута длины стороны используйте метод __setattr__.
    # Новую величину в соответствующем методе необходимо задавать так: super().__setattr__(key, value).
    # Пример будет доступен в дополнительных материалах к курсу.

    def __setattr__(self, key, value):
        # if key in self.protected_attrs:
        if key == "__one":
            raise AttributeError(f"Нельзя установить данный атрибут {key}")

        super().__setattr__(key, value)


# Экземпляр класса
c = Triangle(9, 4, 4)
# print(dir(c))
# c._Triangle_one = 6
# print(c.get_perimetr())
# # c.__one = 6


# Создать еще один класс NewTriangle.
class NewTriangle:
    protected_attrs = ("__one", "__two", "__three")

    def __init__(self, one, two, three):
        self.__one = one
        self.__two = two
        self.__three = three
        self.replace_attr()

    # Но изменять эти атрибуты должно быть возможно только внутри класса предназначенными для этого методами.
    def __setattr__(self, key, value):
        if key in self.protected_attrs:
            raise AttributeError(f"Нельзя установить данный атрибут {key}")
        super().__setattr__(key, value)

    def replace_attr(self):
        self.__one = 5
        self.__two = 7
        self.__three = 11


tr = NewTriangle(6, 7, 2)

try:
    tr.__one = 5
    tr.__two = 7
    tr.__three = 11
except:
    print("Не удается изменить значения")

# Добиться возможности смотреть длину стороны вне класса, обращаясь к его атрибутам.
print(tr._NewTriangle__one, tr._NewTriangle__two, tr._NewTriangle__three, sep="\n")
