class Cat:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return str(3)

    @classmethod
    def from_dog(cls, dog):
        return cls(dog.name)

    @staticmethod
    def meow():
        print('Meow')

    def meow_instance(self):
        print('Meow')


macius = Cat('Maciuś')
macius.meow_instance()
macius.meow()

Cat.meow()
Cat.meow_class()
# Cat.meow_insetnce()


class Dog:
    def __init__(self, name) -> None:
        self.name = name
