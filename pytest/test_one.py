import one

def test_add():
    assert one.add(0, 8) == 8
    assert one.add(-2, -2) == -4
    assert one.add(-1, 4) == 3
    assert one.add(2, 3) == 5

def test_sub():
    assert one.sub(2, 2) == 0
    assert one.sub(2, -2) == 4
    assert one.sub(8, 0) == 8


