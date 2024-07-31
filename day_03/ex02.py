def get_palis(s: set):
    return set(filter(lambda x: x.lower() == x.lower()[::-1], s))


s1 = {'Ala', 'Ola', 'Ula'}

print(get_palis(s1))
