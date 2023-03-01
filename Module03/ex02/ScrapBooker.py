# import sys
# sys.path.append(r"C:/Users/unaib/Desktop/Unibertsitatea/42urduliz/Ai_bootcamp/Module03/ex01/") #r da / ondo irakurtzeko

# from ex import ImageProcessor

#vaya puto lio hau galdetu
import numpy as np

def decorator(function):
    def problem(self, array, dim, position):
        try:
            return(function(self, array, dim, position))
        except:
            return None
    return problem

class ScrapBooker():
    @decorator
    def crop(self, array, dim, position=(0,0)):
        return(np.array([array[i + position[0]][position[1]:position[1] + dim[1]].tolist() for i in range(dim[0])])).__repr__()
        croped = []
        for i in range(dim[0]):
            print(position[0])
            croped.append(array[i + position[0]][position[1]:position[1] + dim[1]].tolist())
        return np.array(croped).__repr__()
    def thin(self, array, n, axis):
        return(np.delete(array, n, axis).__repr__())

spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
arr2 = spb.crop(arr1, (1,3),(1,2))
arr3 = spb.thin(arr1, 1, 0)
print(arr3)