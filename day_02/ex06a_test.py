import ex06

def test_add():
    a = ex06.Point(3,4)
    b = ex06.Point(3,5)
    c = a + b
    assert c.x == 6
    assert c.y == 9


def test_mul():
    a = ex06.Point(3,5)
    b = ex06.Point(1,7)
    c = a * b
    assert c.x == 2
    assert c.y == 6