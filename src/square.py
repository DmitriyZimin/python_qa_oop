from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, length):
        if length <= 0:
            raise ValueError("Длина стороны квадрата должна быть больше '0'")

        super().__init__(length, length)
        self.figure_name = "Квадрат"
