from random import choice, randint


class student():
    def __init__(self, name, surname, faculty, number_checkbook):
        self._name = name
        self._surname = surname
        self._faculty = faculty
        self._number_checkbook = number_checkbook

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def faculty(self):
        return self._faculty

    @property
    def number_checkbook(self):
        return self._number_checkbook

    def print_student(self):
        print(
            "Cтудент", self._name, self._surname, "обучается на факультете",
            self._faculty + ", номер зачётной книжки", str(self._number_checkbook), sep=" ")

    def __eq__(self, other):
        if (self._name == other.name or other.name == "") and (
                self._surname == other.surname or other.surname == "") and (
                self._faculty == other.faculty or other.faculty == "") and (
                self._number_checkbook == other.number_checkbook or other.number_checkbook == ""):
            return True
        else:
            return False


def request():
    print("Введите ... человека которого хотите найти (если хотите пропустить параметр нажмите enter)")
    print("Для поиска по нескольким одноимённым параметрам вводите их через пробел ")
    names = input("Имя ").split(sep=" ")
    surnames = input("Фамилия ").split(sep=" ")
    faculties = input("Факультет ").split(sep=" ")
    number_checkbooks = input("Номер записной книжки ").split(sep=" ")

    students = []
    for name in names:
        for surname in surnames:
            for faculty in faculties:
                for number_checkbook in number_checkbooks:
                    students.append(student(name, surname, faculty, number_checkbook))

    return students


def search(massive):
    searching_students = request()
    for i in range(len(massive)):
        for searching_student in searching_students:
            if massive[i] == searching_student:
                massive[i].print_student()


massive = []
names_gen = ["Александр", "Михаил", "Дмитрий", "Иван", "Роман", "Даниил", "Кирилл", "Максим", "Егор", "Матвей"]
surnames_gen = ["Смирнов", "Иванов", "Кузнецов", "Соколов", "Попов", "Лебедев", "Козлов", "Новиков", "Морозов", "Соловьев"]
faculties_gen = ["ФВТ", "ФИТЭ", "ФПТЭТ"]
max_number_checkbook = 1000
for _ in range(10000):
    massive.append(student(choice(names_gen), choice(surnames_gen), choice(faculties_gen), str(randint(0, max_number_checkbook))))
search(massive)
print("\n" * 5)
for i in range(len(massive)):
    massive[i].print_student()
