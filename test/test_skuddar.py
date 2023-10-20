import pytest
from src.main import is_leapyear

@pytest.mark.parametrize("input_year, result_bool",
[
    (1996, True),
    (2000, True),
    (1700, False),
    (1800, False)
])
def test_the_year_can_be_divided_with_4_but_not_100(input_year, result_bool):
    print(" The year can be divided with 4, but not 100")
    result = is_leapyear(input_year)
    assert result == result_bool

@pytest.mark.parametrize("input_year_2, result_bool_2",
[
    (1800, False),
    (2200, False),
    (1900, False),
    (1200, True),
    (401, False),
    (400, True)
])
def test_the_year_can_be_divided_with_400(input_year_2, result_bool_2):
    print(" The year can be divided with 400")
    result = is_leapyear(input_year_2)
    assert result == result_bool_2

def test_the_year_can_not_be_divided_with_4():
    print(" The year can not be divided with 4")
    assert is_leapyear(1700) == False
    assert is_leapyear(1800) == False
    assert is_leapyear(1602) == False
    assert is_leapyear(1400) == False
    assert is_leapyear(4) == True
    assert is_leapyear(5) == False
    assert is_leapyear(3) == False

@pytest.mark.parametrize("input_year_1, result_bool_1",
[
    (1800, False),
    (2200, False),
    (1900, False),
    (1200, True),
    (400, True),
    (401, False),
    (399, False)
])
def test_the_year_can_be_divided_with_100_but_not_400(input_year_1, result_bool_1):
    print(" The year can be divided with 100, but not with 400")
    result = is_leapyear(input_year_1)
    assert result == result_bool_1
