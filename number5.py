from random import choice, randint


class student():
    def __init__(self, name, surname, faculty, numberCheckbook):
        self.__name = name
        self.__surname = surname
        self.__faculty = faculty
        self.__numberCheckbook = numberCheckbook

    def name(self):
        return self.__name

    def surname(self):
        return self.__surname

    def faculty(self):
        return self.__faculty

    def numberCheckbook(self):
        return self.__numberCheckbook

    def print_student(self):
        print(
            "Cтудент", self.name(), self.surname(), "обучается на факультете", self.faculty()+ ", номер зачётной книжки", str(self.numberCheckbook()),sep=" ")

    def __eq__(self, other):
        if (self.name() == other.name() or other.name() == "") and (self.surname() == other.surname() or other.surname() == "") and (self.faculty() == other.faculty() or other.faculty() == "") and (self.numberCheckbook() == other.numberCheckbook() or other.numberCheckbook() == ""):
            return True
        else:
            return False


def search(massive):
    print("Введите ... человека которого хотите найти (если хотите пропустить параметр нажмите enter)")
    name = input("Имя ")
    surname = input("Фамилия ")
    faculty = input("Факультет ")
    numberCheckbook = input("Номер записной книжки ")

    searchingStudent = student(name, surname, faculty, numberCheckbook)
    for i in range(len(massive)):
        if massive[i] == searchingStudent:
            massive[i].print_student()


massive = []
names = ["Александр", "Михаил", "Дмитрий", "Иван", "Роман", "Даниил", "Кирилл", "Максим", "Егор", "Матвей"]
surnames = ["Смирнов", "Иванов", "Кузнецов", "Соколов", "Попов", "Лебедев", "Козлов", "Новиков", "Морозов", "Соловьев"]
faculties = ["ФВТ", "ФИТЭ", "ФПТЭТ"]
maxNumberCheckbook = 1000
for _ in range(100):
    massive.append(student(choice(names), choice(surnames), choice(faculties), str(randint(0, maxNumberCheckbook))))
search(massive)
print("\n"*5)
for i in range(len(massive)):
    massive[i].print_student()