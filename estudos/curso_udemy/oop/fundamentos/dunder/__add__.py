class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
    def __str__(self):
        return f'({self.x}, {self.y}) # FROM __str__'
    
    def __repr__(self):
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}) # FROM __repr__'
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y
        return result_self > result_other
        
    
if __name__ == '__main__':
    p1 = Ponto(4, 2)
    p2 = Ponto(6, 4)
    p3 = p1 + p2
    print(f'P1: {p1!r}')
    print(f'P2: {p2!r}')
    print(f'P3: {p3!r}')
    print('P1 é maior que P2?', p1 < p2)
    print('P2 é maior que P1?', p2 < p1)