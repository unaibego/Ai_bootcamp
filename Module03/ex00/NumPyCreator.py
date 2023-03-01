import numpy as np

def decorator(function):
    def problem(self, lista):
        try:
            return(function(self, lista))
        except:
            return None
    return problem

class NumPyCreator():
    @decorator
    def from_list(self, lista):
        if (type(lista) != list):
            return None
        return(np.array(lista).__repr__())
    @decorator
    def from_tuple(self, list):
        if (type(list) != tuple):
            return None
        return(np.array(list).__repr__())
    @decorator
    def from_iterable(self, list):
        return(np.arange(list[0], list[-1] + 1).__repr__())
    def from_shape(self, shape, value = 0):
        return(repr(np.ones(shape) * value))
    @decorator
    def random(self, shape):
        return(np.random.rand(shape[0], shape[1]))
    @decorator
    def identity(self, n):
        return(np.identity(n))
array = [1,2,3,4,5]
matrix = [[1,2,3,4],['a','b','c','d', 'y'], [1,2,3,4]]
tuplea = (1,2,3,4)
npc = NumPyCreator()
b = npc.from_list(matrix)
c = npc.from_tuple(matrix)
d = npc.from_shape((7,1), 2)
e = npc.random((7,10))
f = npc.identity((7))
print(f)