import subtraction

def test_subtraction():
    assert subtraction.subtraction([1,1],[2,2])[0] == -1
    assert subtraction.subtraction([1,1],[2,2])[1] == -1
    assert subtraction.subtraction([1,1],[3,5])[0] == -2
    assert subtraction.subtraction([1,1],[3,5])[0] == -4
