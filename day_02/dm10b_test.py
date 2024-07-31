import pytest
import dm10

@pytest.mark.parametrize('a, b, result', [
    (3, 5, 8),
    (13, 15, 28),
    (5, 5, 10),
])
def test_add(a, b, result):
    assert dm10.add(a,b) == result
