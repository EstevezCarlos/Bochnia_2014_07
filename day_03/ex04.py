def englify(text):
    dic = {
        'ą': 'a',
        'ć': 'c',
        'ę': 'e',
        'ł': 'l',
        'ń': 'n',
        'ó': 'o',
        'ś': 's',
        'ż': 'z',
        'ź': 'z',
        'Ą': 'A',
        'Ć': 'C',
        'Ę': 'E',
        'Ł': 'L',
        'Ń': 'N',
        'Ó': 'O',
        'Ś': 'S',
        'Ż': 'Z',
        'Ź': 'Z',
    }

    # return ''.join(map(lambda c: dic[c] if c in dic else c, text))
    return ''.join(map(lambda c: dic.get(c, c), text))


print(englify('Bąk brzęczy, wół bączy.'))
