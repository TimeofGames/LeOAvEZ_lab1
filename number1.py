from random import randint


def create_massive(minimum, maximum, lenght):
    return list(randint(minimum, maximum) for _ in range(lenght))


massive = create_massive(int(input("Введите минимальное число ")), int(input("Введите максимальное число ")), int(input("Введите длину массива ")))
massive.sort()
print(massive[-1]-massive[0])