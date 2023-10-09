import pytest


def test_equal(test_func):
    assert 1 == 1, 'Numbres not equal'
    print(test_func)
def test_equal2():
    assert 1 == 1, 'Numbers not equal'

# skip the test
@pytest.mark.skip('It is the develop functional')
def test_sum():
    assert 5 + 5 == 8 + 2


def test_calc(calc):
    print(calc(200, 500))

@pytest.mark.parametrize("first_value, second_value, result", [(1, 2, 3), (4, 40,  44), (5, 100, 105), (10, 10, 20)])
def test_calculator(first_value, second_value, result, calc):
    assert calc(first_value, second_value) == result


