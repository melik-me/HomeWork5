# Прямоугольная площадка (пример: комната) (свойства: две стороны)
# Нужно высчитать: площадь, периметр.

from math import atan, pi, sin, cos

class Room:
    """This class describes rectangular room."""

    def __init__(self, length=0.0, width=0.0):
        self.length = length
        self.width = width

    def area(self):
        """This method returns the area of the room."""
        return self.length * self.width

    def perimeter(self):
        """This method returns the perimeter of the room."""
        return (self.length + self.width) * 2


l = float(input("Please enter the length of the room.\n"))
w = float(input("Please enter the width of the room.\n"))

r = Room(l, w)
print("The area of a room is {0:.2f}.".format(r.area()))
print("The perimeter of the room is {0:.2f}.".format(r.perimeter()))


# Точка на карте (свойства: X, Y).
# Вычислить расстояние до начала координат.
# Расстояние до другой точки, экземпляра этого же класса.
# Перевод в другие системы координат.

class Dot:
    """This class described a dot in Descartes coordinate system."""

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def center(self):
        return (self.x**2 + self.y**2)**0.5

    def distance(self, d):
        return ((d.x - self.x)**2 + (d.y - self.y)**2)**0.5

    def polar(self):
        r = self.center()

        f = 0.0
        if self.x == self.y == 0:
            f = 0.0
        elif self.x == 0 and self.y < 0:
            f = 3 * pi / 2
        elif self.x == 0 and self.y > 0:
            f = pi / 2
        elif self.x < 0:
            f = atan(self.y / self.x) + pi
        elif self.x > 0 and self.y < 0:
            f = atan(self.y / self.x) + 2*pi
        else:
            f = atan(self.x / self.y)
        self.x = r
        self.y = f

    def decart(self):
        x = self.x * cos(self.y)
        y = self.x * sin(self.y)
        self.x = x
        self.y = y

d1 = Dot(4, 4)
d2 = Dot(10, 10)

print("The distance between first dot and center is {0:.2f}.".format(d1.center()))
print("The distance between first and second dots is {0:.2f}.".format(d1.distance(d2)))
d1.polar()
print("First dot in polar coordinate system is {0:.2f}, {1:.2f}.".format(d1.x, d1.y))
d1.decart()
print("Back to Descartes: {0:.2f}, {1:.2f}.".format(d1.x, d1.y))