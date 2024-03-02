import pytest

from src.rectangle import Rectangle


@pytest.mark.parametrize(
    "rectangle_length, rectangle_width, rectangle_name",
    [(1, 1, "Прямоугольник")]
)
class TestRectangleInit:
    def test_rectangle_init_positive(self, rectangle_length, rectangle_width, rectangle_name):
        rectangle = Rectangle(rectangle_length, rectangle_width)
        assert rectangle.figure_name == rectangle_name, "Неправильное название прямоугольника"
        assert rectangle.length == rectangle_length, "Некорректная длина"
        assert rectangle.width == rectangle_width, "Некорректная ширина"


@pytest.mark.parametrize("rectangle_length", [5])
@pytest.mark.parametrize("rectangle_width", [6])
class TestRectanglePositive:
    @pytest.mark.parametrize("expected_area", [30])
    def test_rectangle_area_positive(self, rectangle_length, rectangle_width, expected_area):
        rectangle = Rectangle(rectangle_length, rectangle_width)
        assert rectangle.area == expected_area

    @pytest.mark.parametrize("expected_perimeter", [22])
    def test_rectangle_perimeter_positive(self, rectangle_length, rectangle_width, expected_perimeter):
        rectangle = Rectangle(rectangle_length, rectangle_width)
        assert rectangle.perimeter == expected_perimeter


@pytest.mark.parametrize(
    "rectangle_length, rectangle_width",
    [(0, 6), (5, 0), (-1, 6), (5, -1)]
)
class TestRectangleNegative:
    def test_rectangle_init_negative(self, rectangle_length, rectangle_width):
        with pytest.raises(ValueError, match="Сторона прямоугольника должна быть больше '0'"):
            Rectangle(rectangle_length, rectangle_width)
