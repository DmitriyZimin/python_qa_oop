import math

import pytest

from src.circle import Circle


@pytest.mark.parametrize(
    "circle_radius, circle_name",
    [(1, "Круг")]
)
class TestCircleInit:
    def test_circle_init_positive(self, circle_radius, circle_name):
        circle = Circle(circle_radius)
        assert circle.figure_name == circle_name, "Неправильное название круга"
        assert circle.radius == circle_radius, "Некорректный радиус"


@pytest.mark.parametrize("circle_radius", [6])
class TestCirclePositive:

    def test_circle_area_positive(self, circle_radius):
        circle = Circle(circle_radius)
        assert circle.area == math.pi * circle_radius ** 2

    def test_circle_perimeter_positive(self, circle_radius):
        circle = Circle(circle_radius)
        assert circle.perimeter == 2 * math.pi * circle_radius


@pytest.mark.parametrize(
    "circle_radius",
    [0, -1]
)
class TestCircleNegative:
    def test_circle_init_negative(self, circle_radius):
        with pytest.raises(ValueError, match="Радиус круга должен быть больше '0'"):
            Circle(circle_radius)
