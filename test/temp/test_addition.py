import addition


def test_addition():
    assert addition.addition([1, 1], [2, 2])[0] == 3
    assert addition.addition([1, 1], [2, 2])[1] == 3
    assert addition.addition([1, 1], [3, 5])[0] == 4
    assert addition.addition([1, 1], [3, 5])[1] == 6
