# Задание 6

# Это уже было, но теперь оформите это функцией:

# Написать функцию is_year_leap, принимающую 1 аргумент — год, и
# возвращающую True, если год високосный, и False иначе.

def is_year_leap(year):

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input(""" — Hey, Doc!
     — Hey, Marty! Are you ready? We are going to [please enter a year]!\n"""))
    b = is_year_leap(n)

    print(b)

# Функция принимает три числа a, b, c. Функция должна определить,
# существует ли треугольник с такими сторонами. Если треугольник
# уществует, вернёт True, иначе False.

def does_it_exist(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

if __name__ == "__main__":
    x = float(input("Please enter first side of the triangle:\n"))
    y = float(input("Please enter second side of the triangle:\n"))
    z = float(input("Please enter third side of the triangle:\n"))

    b = does_it_exist(x, y, z)

    print(b)
