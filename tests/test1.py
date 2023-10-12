import pytest

@pytest.mark.development
def test_equal(test_func):
    assert 1 == 1, 'Numbres not equal'
    print(test_func)
@pytest.mark.development
def test_equal2():
    assert 1 == 1, 'Numbers not equal'

# skip the test
@pytest.mark.skip('It is the develop functional')
def test_sum():
    assert 5 + 5 == 8 + 2


def test_calc(calc):
    print(calc(200, 500))
@pytest.mark.development
@pytest.mark.parametrize("first_value, second_value, result", [(1, 2, 3), (4, 40,  44), (5, 100, 105), (10, 10, 20)])
def test_calculator(first_value, second_value, result, calc):
    assert calc(first_value, second_value) == result

@pytest.mark.production
@pytest.mark.parametrize('result, values, comment', [
    (True, 7, ''),
    (False, 10, 'cool!'),
    (None, 5, 'Hello')
])
def test_values(result, values, comment, test_json):
    var = test_json
    var.set_result(result).set_values(values).set_comment(comment)
    print(var.json)






# commands
# pytest -s -v -k production  tests/test1.py
# pytest -s -v -k development  tests/test1.py
# pytest -s -v -k 'not production'  tests/test1.py
# pytest -s -v tests/test1.pytest
# pytest -s -v --durations=3 tests/test1.py
# pytest -s -v --durations=3 -vv tests/test1.py
#  sudo  apt install allure
# pip3 install allure-pytest
# pytest -s -v tests/test1.py --alluredir=tests/alluretest
#