def week_str_to_int(day: str) -> int:
    """
    Funkcja zwracająca numer dnia tygodnia na podstawie nazwy.
    Używa ifów i elifów.
    """
    if day == "pn":
        return 1
    elif day == "wt":
        return 2
    elif day == "śr":
        return 3
    elif day == "cz":
        return 4
    elif day == "pt":
        return 5
    elif day == "sb":
        return 6
    elif day == "nd":
        return 7
    else:
        return None


def week_str_to_int_better(day: str) -> int:
    """
    Funkcja zwracająca numer dnia tygodnia na podstawie nazwy.
    Używa tablicy prawdy, ale do wyświetlenia wartości domyślnej używa ifa.
    """
    week_dict = {
        "pn": 1,
        "wt": 2,
        "śr": 3,
        "cz": 4,
        "pt": 5,
        "sb": 6,
        "nd": 7,
    }
    return week_dict[day] if day in week_dict else None


def week_str_to_int_the_best(day: str) -> int:
    """
    Funkcja zwracająca numer dnia tygodnia na podstawie nazwy.
    Używa tablicy prawdy, i do wyświetlenia wartości domyślnej używa get.
    """
    week_dict = {
        "pn": 1,
        "wt": 2,
        "śr": 3,
        "cz": 4,
        "pt": 5,
        "sb": 6,
        "nd": 7,
    }
    return week_dict.get(day, None)
