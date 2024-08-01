NOW = 2024

class Dog:
    species = 'dog'

    def __init__(self, name, date_of_birth, race) -> None:
        self.name = name
        self.age = NOW - date_of_birth
        self._race = race

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age < 20:
            self.age = age
        else:
            raise ValueError('Dogs, don\'t live that long.')
        
    def age_this_dog(self):
        self.age += 1

    

fifi = Dog('Fifi', 2020, 'Beagle')

print(fifi.get_age())