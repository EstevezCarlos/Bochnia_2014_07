import ex05


def test_dog_a():
    doge = ex05.dog_a
    assert doge.name == 'Burek'
    assert ex05.dog_a().age == 5
    assert ex05.dog_a().race == 'Jamnik'
    assert ex05.dog_a().sex == True
    assert ex05.dog_a().noise == 'hau hau'
    ex05.dog_a
