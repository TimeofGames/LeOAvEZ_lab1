from random import randint


class Matrix():
    def __init__(self):
        self.minimum = int(input("Введите минимальное число "))
        self.maximum = int(input("Введите максимальное число "))
        self.strings = int(input("Введите количество строк "))
        self.rows = int(input("Введите количество столбцов "))
        self.data = [[randint(self.minimum, self.maximum) for _ in range(self.rows)] for _ in range(self.strings)]

    def print_matrix(self):
        lenght = len(str(self.maximum))+1
        print(("+" + "-" * lenght) * (self.rows+1)+"+")
        for i in range(self.strings):
            for j in range(self.rows):
                print(("|{:^" + str(lenght) + "}").format(self.data[i][j]), end="")
            print(("|{:^" + str(lenght) + "}|").format(str(sum(self.data[i]))))
            print(("+" + "-" * lenght) * (self.rows+1)+"+")
        for i in range(self.rows):
            print(("|{:^" + str(lenght) + "}").format(sum([self.data[j][i] for j in range(self.strings)])), end="")

        print("|"+" "*lenght +"|\n"+("+" + "-" * lenght) * (self.rows+1)+"+")


matrix = Matrix()
matrix.print_matrix()
