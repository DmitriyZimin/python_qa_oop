from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, figure):
        self.figure = figure

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Передана не геометрическая фигура")
        return self.area + figure.area
