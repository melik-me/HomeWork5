# Задание 7

# Функция принимает три числа a, b, c. Функция должна определить, существует
# ли треугольник с такими сторонами и если существует, то возвращает тип
# треугольника Equilateral triangle (равносторонний), Isosceles triangle
# (равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not
# a triangle).

def who_are_you_dude(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        e = True
    else:
        e = False

    if e:
        if a == b == c:
            s = "Equilateral triangle"
        elif a == b or b == c or a == c:
            s = "Isosceles triangle"
        else:
            s = "Versatile triangle"
    else:
        s = "Not a triangle"

    return s

if __name__ == "__main__":
    x = float(input("Please enter first side of the triangle:\n"))
    y = float(input("Please enter second side of the triangle:\n"))
    z = float(input("Please enter third side of the triangle:\n"))

    print(who_are_you_dude(x, y, z))
