import pytest
import dm10

@pytest.fixture
def my_data():
    return [3,4,7]

@pytest.fixture
def random_data():
    return [5,10,15]

def test_add(my_data):
    assert dm10.add(my_data[0],my_data[1]) == my_data[2]


def test_add_2(random_data):
    assert dm10.add(random_data[0],random_data[1]) == random_data[2]