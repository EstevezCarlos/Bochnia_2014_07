import dm11


def test_my_fun(capfd):
    dm11.my_fun()
    out, err = capfd.readouterr()
    assert out == 'yolo\n'
