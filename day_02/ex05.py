from typing import Any


class Dog():
    def __init__(self, name:str, age:int, race:str, sex:bool, noise:str) -> None:
        self.name = name
        self.age = age
        self.race = race
        self.sex = sex
        self.noise = noise

    def __str__(self) -> str:
        return f'{"Pies" if self.sex else "Suka"} {self.name} rasy {self.race}'

    def __add__(self, other):
        return self.age + other.age

    def __call__(self):
        self.bark()

    def bark(self):
        print(self.noise)

dog_a = Dog("Burek", 5, "Jamnik", True, 'hau hau')
dog_b = Dog("Cola", 4, "Beagle", False ,"woof woof")
# dog_c = Dog("Reksio", 3, "Pudel", True, "WOOOF!")
# dog_d = Dog("Koka", 2, "Chiuaua", False, "wrrr")

print(dog_a)
print(dog_b)
print(dog_a + dog_b)
dog_a()

del dog_a