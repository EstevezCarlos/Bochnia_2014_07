class Dog():
    def __init__(self) -> None:
        self.age = 0
        self.name = ''
        pass

    def set_age(self, age):
        self.set_age = age
        return self

    def set_name(self, name):
        self.set_name = name
        return self
    
fifi = Dog().set_name('Fifi').set_age(8)