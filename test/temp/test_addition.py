import addition

def test_addition():
    assert addition.addition([1,1],[2,2]) == [3,3]
    assert addition.addition([1,1],[3,5]) == [4,6]
