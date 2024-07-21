from math import sqrt, pi


class Shape:

    def area(self) -> int | float:
        pass


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self) -> int | float:
        half_perimeter = (self.a + self.b + self.c) / 2
        return sqrt(half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (half_perimeter - self.c))

    def is_right_angled(self) -> bool:
        return (self.a**2 + self.b**2 == self.c**2
                or self.a**2 + self.c**2 == self.b**2
                or self.b**2 + self.c**2 == self.a**2)


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self) -> int | float:
        return pi * self.radius ** 2


def area_in_compile_time(shape: Shape):
    return shape.area()
