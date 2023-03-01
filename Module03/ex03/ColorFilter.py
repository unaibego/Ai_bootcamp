import matplotlib.image as mpimg
import matplotlib.pyplot

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
img.display(array)