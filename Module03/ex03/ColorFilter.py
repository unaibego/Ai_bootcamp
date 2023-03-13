import matplotlib.image as mpimg
import matplotlib.pyplot
import numpy as np

def decorator(function):
    def problem(self, lista):
        try:
            return(function(self, lista))
        except:
            print("Exception: FileNotFoundError -- strerror: No such file or directory")
            return None
    return problem

class ColorFilter():
    def invert(self, array):
        return (1 - array)
    def to_blue(self, array):
        array[:, :, 0] = np.zeros(np.shape(array[:, :, 0]))
        array[:, :, 1] = np.zeros(np.shape(array[:, :, 2]))
        return (array)
    def to_green(self, array):
        array[:, :, 0] = array[:, :, 0] * 0
        array[:, :, 2] = array[:, :, 2] * 0
        return (array)
    def to_red(self, array):
        # blue_array = self.to_blue(array)
        # green_array = self.to_green(array)
        array[:, :, 1] = array[:, :, 1] - array[:, :, 1]
        array[:, :, 2] = array[:, :, 2] - array[:, :, 2]
        return (array)

        
#bertan shape-k ez ditu parentesiak atributo bat delako. Hau da, "self.shape" moduan definitu dute numpyko sortzaileak eta ez "def shape"
class ImageProcesor():
    @decorator
    def load(self, path):
        rgb_array = mpimg.imread(path)
        print(f"Loading image of dimensions {rgb_array.shape[0]} x {rgb_array.shape[1]}")
        return(rgb_array)
    @decorator
    def display(self, array):
        matplotlib.pyplot.imshow(array)
        matplotlib.pyplot.show()






img = ImageProcesor()
array = img.load("Cute_acab.png")
cf = ColorFilter()
# array = cf.invert(array)
array = cf.to_red(array)
img.display(array)