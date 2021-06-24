import division
import multiplication


def test_multiplication():
    assert multiplication.multiplication([1, 1], [2, 2])[0] == 2
    assert multiplication.multiplication([1, 1], [2, 2])[1] == 2
    assert multiplication.multiplication([1, 1], [3, 5])[0] == 3
    assert multiplication.multiplication([1, 1], [3, 5])[1] == 5


def test_division():
    assert division.division([1, 1], [2, 2])[0] == 0.5
    assert division.division([1, 1], [2, 2])[1] == 0.5
    assert division.division([1, 1], [4, 5])[0] == 0.25
    assert division.division([1, 1], [3, 5])[1] == 0.2
