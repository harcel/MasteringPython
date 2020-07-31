import numpy as np
class Vector():
    """Class for vectors"""
    # 1: the init defines the components
    def __init__(self, vect):
        self.components = np.array(vect)
        self.length = len(vect)
    
    # 1: __len__ does not exist for built-ins, but you can make it!
    def __len__(self):
        return self.length
    
    # 2: it's easy, IF the vector components are numpy arrays of equal length
    def __add__(self, other):
        # It's made a vector again itself, of course!
        return Vector(self.components + other.components)
           
    # 3: __str__ 
    def __str__(self):
        return " ".join(self.components.astype('str'))
    
    # 3: __repr__ is used for debugging or showing the call sequence
    def __repr__(self):
        return 'Vector({0})'.format(self.components)    
    
    # 4: Multiplication is implemented with __mul__
    def __mul__(self, other):
        return np.sum(self.components * other.components)
        
    # 5: absolute values come from the __abs__ dunder method
    def __abs__(self):
        return np.sqrt(np.sum(self.components**2))
    
 
        
a = Vector([3, 4])
b = Vector([1, 0])
print(a+b)
print(a)
print(abs(a))
print(a*b)
a   # Note the difference between the __str__ and __repr__ methods! 
