class Ponto:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z}) # FROM __str__'
    
    def __repr__(self):
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r}) # FROM __repr__'

p1 = Ponto(1, 2, 'String')
p2 = Ponto(978, 876, 'String')

print(p1) # __str__
print(repr(p2)) # __repr__

print(f'{p1!r}') # __repr__
print(f'{p1!s}') # __str__
