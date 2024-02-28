import pytest

from src.rectangle import Rectangle
from src.square import Square


@pytest.mark.parametrize(
    "rectangle_length, rectangle_width, square_length, expected_add_area",
    [(2, 3, 5, 31), (3, 4, 4, 28)]
)
class TestFigurePositive:

    def test_add_area_positive(self, rectangle_length, rectangle_width, square_length, expected_add_area):
        rectangle = Rectangle(rectangle_length, rectangle_width)
        square = Square(square_length)
        assert rectangle.add_area(square) == expected_add_area


@pytest.mark.parametrize(
    "rectangle_length, rectangle_width, letter",
    [(5, 6, 'b')]
)
class TestFigureNegative:

    def test_add_area_negative(self, rectangle_length, rectangle_width, letter):
        figure = letter
        rectangle = Rectangle(rectangle_length, rectangle_width)
        with pytest.raises(ValueError, match="Передана не геометрическая фигура"):
            rectangle.add_area(figure)
