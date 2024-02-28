import pytest

from src.square import Square


@pytest.mark.parametrize(
    "square_length, square_name",
    [(1, "Квадрат")]
)
class TestSquareInit:
    def test_square_init_positive(self, square_length, square_name):
        square = Square(square_length)
        assert square.figure_name == square_name, "Неправильное название квадрата"
        assert square.length == square_length, "Некорректная длина стороны"


@pytest.mark.parametrize("square_length", [5])
class TestSquarePositive:
    @pytest.mark.parametrize("expected_area", [25])
    def test_square_area_positive(self, square_length, expected_area):
        square = Square(square_length)
        assert square.area == expected_area

    @pytest.mark.parametrize("expected_perimeter", [20])
    def test_square_perimeter_positive(self, square_length, expected_perimeter):
        square = Square(square_length)
        assert square.perimeter == expected_perimeter


@pytest.mark.parametrize("square_length", [0, -1])
class TestSquareNegative:
    def test_square_init_negative(self, square_length):
        with pytest.raises(ValueError, match="Длина стороны квадрата должна быть больше '0'"):
            Square(square_length)
