from random import choice, randint


class student():
    def __init__(self, name, surname, faculty, numberCheckbook):
        self.__name = name
        self.__surname = surname
        self.__faculty = faculty
        self.__number_checkbook = numberCheckbook

    def name(self):
        return self.__name

    def surname(self):
        return self.__surname

    def faculty(self):
        return self.__faculty

    def number_checkbook(self):
        return self.__number_checkbook

    def print_student(self):
        print(
            "Cтудент", self.name(), self.surname(), "обучается на факультете",
            self.faculty() + ", номер зачётной книжки", str(self.number_checkbook()), sep=" ")

    def __eq__(self, other):
        if (self.name() == other.name() or other.name() == "") and (
                self.surname() == other.surname() or other.surname() == "") and (
                self.faculty() == other.faculty() or other.faculty() == "") and (
                self.number_checkbook() == other.number_checkbook() or other.number_checkbook() == ""):
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
maxNumberCheckbook = 1000
for _ in range(100):
    massive.append(student(choice(names_gen), choice(surnames_gen), choice(faculties_gen), str(randint(0, maxNumberCheckbook))))
search(massive)
print("\n" * 5)
for i in range(len(massive)):
    massive[i].print_student()
