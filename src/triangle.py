import math

from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b < side_c or side_b + side_c < side_a or side_a + side_c < side_b:
            raise ValueError("Треугольник не существует")

        super().__init__("Треугольник")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self):
        half_perimeter = self.perimeter * 0.5
        return math.sqrt(half_perimeter * (half_perimeter - self.side_a) * (half_perimeter - self.side_b) * (
                half_perimeter - self.side_c))
