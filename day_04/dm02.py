class Cat:

    def __init__(self, name, race) -> None:
        self.name = name
        self._race = race

    def __str__(self):
        return f"Kot o imieniu {self.name}."

    def __repr__(self):
        return f"Instancja klasy [Cat] Kot o imieniu {self.name}."

gato = Cat('Gato','ragdoll')

print(gato)
print(repr(gato))
