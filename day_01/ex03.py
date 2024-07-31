def plcie(*imiona):
    """
    Funkcja przymuje dowoloną ilość arggumentów, jeśli wszystkie stringi kończą się na 'a', to wtedy zwraca kobiety.
    Jeśli żaden ze stringów nie konczy się na 'a', to zwraca mężczyźni. W przeciwnym wypadku zwraca mieszane.
    """
    women = 0
    men = 0
    slownik = {
        (False, False): "",
        (True, False): "Kobiety",
        (False, True): "Mężczyźni",
        (True, True): "Mieszane",
    }
    for imie in imiona:
        if imie.endswith("a"):
            women += 1
        if not imie.endswith("a"):
            men += 1
    return slownik[bool(women), bool(men)]

    # 00000 domyślny int
    # 00001 jeżeli są kobiety podmieniamy ostatnie zero na 1
    # 00010 jeżeli są mężczyźni podmieniamy przedostatnie zero na 1
    # 00011
