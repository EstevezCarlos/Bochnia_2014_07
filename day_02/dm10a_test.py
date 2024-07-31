import dm10

def test_add():
    assert dm10.add(3,5) == 8
    assert dm10.add(5,5) == 10
    assert dm10.add(13,15) == 28

def test_upper():
    assert dm10.up_my_str('qwe ASD') == 'QWE ASD'

def test_ten_to_twenty():
    set_of_results = set()
    for _ in range(30000):
        result = dm10.ten_to_twenty()
        set_of_results.add(result)
        assert result >= 10
        assert result <= 20
    assert len(set_of_results) == 11, 'Jest mała szansa, że ten test uruchomiony ponownie jednak przejdzie.'