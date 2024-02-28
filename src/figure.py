from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, figure_name):
        self.figure_name = figure_name

    @property
    @abstractmethod
    def area(self):
        raise NotImplementedError("Метод area не реализован")

    @property
    @abstractmethod
    def perimeter(self):
        raise NotImplementedError("Метод perimeter не реализован")

    def add_area(self, figure_name):
        if not isinstance(figure_name, Figure):
            raise ValueError("Передана не геометрическая фигура")
        return self.area + figure_name.area
