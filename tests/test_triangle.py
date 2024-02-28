import pytest

from src.triangle import Triangle


@pytest.mark.parametrize("triangle_side_a", [3])
@pytest.mark.parametrize("triangle_side_b", [4])
@pytest.mark.parametrize("triangle_side_c", [5])
class TestTrianglePositive:
    @pytest.mark.parametrize("triangle_name", ["Треугольник"])
    def test_triangle_init_positive(self, triangle_side_a, triangle_side_b, triangle_side_c, triangle_name):
        triangle = Triangle(triangle_side_a, triangle_side_b, triangle_side_c)
        assert triangle.figure_name == triangle_name, "Неправильное название треугольника"
        assert triangle.side_a == triangle_side_a, "Некорректная сторона a"
        assert triangle.side_b == triangle_side_b, "Некорректная сторона b"
        assert triangle.side_c == triangle_side_c, "Некорректная сторона c"

    @pytest.mark.parametrize("expected_area", [6])
    def test_triangle_area_positive(self, triangle_side_a, triangle_side_b, triangle_side_c, expected_area):
        triangle = Triangle(triangle_side_a, triangle_side_b, triangle_side_c)
        assert triangle.area == expected_area

    @pytest.mark.parametrize("expected_perimeter", [12])
    def test_triangle_perimeter_positive(self, triangle_side_a, triangle_side_b, triangle_side_c, expected_perimeter):
        triangle = Triangle(triangle_side_a, triangle_side_b, triangle_side_c)
        assert triangle.perimeter == expected_perimeter


@pytest.mark.parametrize("triangle_side_a", [1])
@pytest.mark.parametrize("triangle_side_b", [20])
@pytest.mark.parametrize("triangle_side_c", [25])
class TestTriangleNegative:
    def test_triangle_init_negative(self, triangle_side_a, triangle_side_b, triangle_side_c):
        with pytest.raises(ValueError, match="Треугольник не существует"):
            Triangle(triangle_side_a, triangle_side_b, triangle_side_c)
