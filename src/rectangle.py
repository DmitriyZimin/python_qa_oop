from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, length, width):
        if length <= 0:
            raise ValueError("Сторона прямоугольника должна быть больше '0'")
        if width <= 0:
            raise ValueError("Сторона прямоугольника должна быть больше '0'")
        super().__init__("Прямоугольник")
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return (self.length + self.width) * 2
