import pytest

# autouse == выполнение фикстуры для всех тестов
# scope = function - выполнение функции каждый раз при вызове
# scope = session - выполнение функции один раз, после результат кэшируется и возврщ одно и тоже значение
@pytest.fixture()
def test_func():
    print("It's the test function")