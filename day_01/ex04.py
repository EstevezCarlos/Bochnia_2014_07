def get_sex(imie, wiek):
    """
    Klasyfikuje osobę na podstawie imienia i wieku.
    """
    czy_kobieta = imie.lower().endswith("a")
    czy_pelnoletni = wiek > 18

    warunki = (czy_kobieta, czy_pelnoletni)

    mozliwe_wybory = {
        (True, True): "kobieta",
        (False, True): "mężczyzna",
        (True, False): "dziewczyna",
        (False, False): "chłopak",
    }

    return mozliwe_wybory[warunki]
