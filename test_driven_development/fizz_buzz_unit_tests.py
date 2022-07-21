from test_driven_development.fizz_buzz import fizz_buzz
import pytest


@pytest.mark.parametrize("input_int", [3, 6])
def test_print_fizz_when_n_is_3(input_int):
    output = fizz_buzz(input_int)
    assert output == "Fizz"


@pytest.mark.parametrize("input_int", [5, 10])
def test_print_buzz_when_n_is_5(input_int):
    output = fizz_buzz(input_int)
    assert output == "Buzz"


@pytest.mark.parametrize("input_int", [15, 30])
def test_print_fizz_buzz_when_n_is_15(input_int):
    output = fizz_buzz(input_int)
    assert output == "FizzBuzz"


@pytest.mark.parametrize("input_int,expected_out", ([1, 1], [2, 2]))
def test_print_n(input_int,expected_out):
    output = fizz_buzz(input_int)
    assert output == expected_out


@pytest.mark.parametrize("input_int", [0.1, -3])
def test_non_positive_input(input_int):
    output = fizz_buzz(input_int)
    assert output == "Input must be positive integer"
