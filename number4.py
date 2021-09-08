from random import randint


class Matrix():
    def __init__(self):
        self._minimum = int(input("Введите минимальное число "))
        self._maximum = int(input("Введите максимальное число "))
        self._strings = int(input("Введите количество строк "))
        self._rows = int(input("Введите количество столбцов "))
        self._data = [[randint(self._minimum, self._maximum) for _ in range(self._rows)] for _ in range(self._strings)]

    @property
    def minimum(self):
        return self._minimum

    @property
    def maximum(self):
        return self._maximum

    @property
    def strings(self):
        return self._strings

    @property
    def rows(self):
        return self._rows

    @property
    def data(self):
        return self._data

    def print_matrix(self):
        lenght = len(str(self._maximum)) + 1
        print(("+" + "-" * lenght) * (self._rows + 1) + "+")
        for i in range(self._strings):
            for j in range(self._rows):
                print(("|{:^" + str(lenght) + "}").format(self._data[i][j]), end="")
            print(("|{:^" + str(lenght) + "}|").format(str(sum(self._data[i]))))
            print(("+" + "-" * lenght) * (self._rows + 1) + "+")
        for i in range(self._rows):
            print(("|{:^" + str(lenght) + "}").format(sum([self._data[j][i] for j in range(self._strings)])), end="")

        print("|" + " " * lenght + "|\n" + ("+" + "-" * lenght) * (self._rows + 1) + "+")


matrix = Matrix()
matrix.print_matrix()
