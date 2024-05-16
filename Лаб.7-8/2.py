# Даны два файла (в Moodle) формата csv и json, содержащие разные списки городов, их население, регион и индекс.

# Данные из файлов необходимо соединить таким образом, чтобы они содержали только уникальные значения.

# Для этого создайте класс City, у которого будут реализованы методы __hash__ и __eq__.

# Поместите экземпляры класса в коллекцию, при правильно реализованных вышеуказанных методов коллекция будет содержать только уникальные города.

# Новый список городов необходимо сохранить в форматы CSV и JSON.
# Используйте собственные функции преобразований.

import csv, json


class City:
    def __init__(self, index, tregion, region, city, pop):
        self.index = index
        self.tregion = tregion
        self.region = region
        self.city = city
        self.pop = pop

    def __str__(self) -> str:
        return f"name: {self.index}, tregion: {self.tregion}, region: {self.region}, city: {self.city}, population: {self.pop}"

    def __repr__(self) -> str:
        return f"City({self.index}): {self}"

    def __eq__(self, other):
        if isinstance(other, City):
            return self.index == other.index
        return False

    def __hash__(self) -> int:
        return hash(self.index)

    # ----------------------------------------ДОПОЛНИТЕЛЬНО--------------------------------------
    # Перед сохранением данных в файл отсортируйте список по численности населения.
    def __gt__(self, other):
        if isinstance(other, City):
            return self.pop > other.pop
        return False


list1 = []

with open(
    "Города.csv",
    "r",
    newline="",
    encoding="utf-8",
) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row["index"] = row.pop("Индекс")
        row["tregion"] = row.pop("Тип региона")
        row["region"] = row.pop("Регион")
        row["city"] = row.pop("Город")
        row["pop"] = row.pop("Население")
        if row["pop"].isdigit() == True:
            row["pop"] = int(row["pop"])
            list1.append(row)
        else:
            s = [i for i in row["pop"] if i.isdigit() != True]
            for el in s:
                row["pop"] = row["pop"].replace(el, "")
            row["pop"] = int(row["pop"])
            list1.append(row)

list_city = [City(**p) for p in list1]
list_city = list(set(list_city))

# Для чтения в модуле json есть два метода:

# json.load - метод считывает файл в формате JSON и возвращает объекты Python
# json.loads - метод считывает строку в формате JSON и возвращает объекты Python

# Чтение файла json
with open("города.json", "r", encoding="utf-8") as f:
    city = json.load(f)
# print(city)

for section, commands in city.items():
    # print(section)
    for c in commands:
        c["index"] = c.pop("Индекс")
        c["tregion"] = c.pop("Тип региона")
        c["region"] = c.pop("Регион")
        c["city"] = c.pop("Город")
        c["pop"] = c.pop("Население")
        if type(c["pop"]) == str:
            s = [i for i in c["pop"] if i.isdigit() != True]
            for el in s:
                c["pop"] = c["pop"].replace(el, "")
            c["pop"] = int(c["pop"])
            c = City(**c)
            list1.append(c)
        else:
            c = City(**c)
            list1.append(c)


list_city.sort()
print(len(list_city))

# --------------------------------------------ПРОВЕРКА-------------------------------------------------------


# for l in list_city[0:5]:
#     print(l.pop)


# for dicts in list1:
#     if dicts["pop"] == 963:
#         print(dicts)


# --------------------------------------------ЗАПИСЬ ФАЙЛА (CSV и JSON)-------------------------------------------------------

# writerow - записывает каждый список построчно;
# writerows - записывает список списков в файл целиком.

lines = [i.__dict__ for i in list_city]


with open("City_newfile.csv", "w+", newline="", encoding="utf-8") as new_file:
    writer = csv.DictWriter(
        new_file,
        fieldnames=["Индекс", "Тип региона", "Регион", "Город", "Население"],
    )
    writer.writeheader()
    for line in lines:
        line["Индекс"] = line.pop("index")
        line["Тип региона"] = line.pop("tregion")
        line["Регион"] = line.pop("region")
        line["Город"] = line.pop("city")
        line["Население"] = line.pop("pop")
        writer.writerow(line)


# Для записи информации в формате JSON в модуле json также два метода:

# json.dump - метод записывает объект Python в файл в формате JSON
# json.dumps - метод возвращает строку в формате JSON


# Параметр ensure_ascii в функции json.dumps() по умолчанию установлен в True. Это приводит к преобразованию не-ASCII символов в escape-последовательности.

# Если установить этот параметр в False, то функция json.dumps() будет сохранять все символы в исходном виде.

data = {"City": [i for i in lines]}


with open("City_newfile.json", "w", encoding="utf-8") as new_file:
    json.dump(data, new_file, indent=2, ensure_ascii=False)
    # new_file.write(json.dumps(data, indent=2, ensure_ascii=False))


# Хеши используются для быстрого сравнения ключей словаря во время поиска по нему.
# Хеш - это результат хеширования, т.е. операции по преобразованию данных в строку или число фиксированной длины.
