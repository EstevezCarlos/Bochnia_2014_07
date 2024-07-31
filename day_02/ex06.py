class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'Point(x: {self.x}, y: {self.y})'
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        x = (self.x + other.x) / 2
        y = (self.y + other.y) / 2
        return Point(x, y)
    
    def _size(self, other):
        self_z = ((self.x**2) + (self.y**2))**(1/2)
        other_z = ((other.x**2) + (other.y**2))**(1/2)
        return self_z, other_z
    
    def __eq__(self, other) -> bool:
        self_z, other_z = self._size(other)
        return self_z == other_z
    
    def __gt__(self, other) -> bool:
        self_z, other_z = self._size(other)
        return self_z > other_z