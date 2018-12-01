from src import calculator


def test_add():
    assert calculator.add(2, 2) == 4


def test_substract():
    assert calculator.substract(4, 2) == 2
