from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import datasets, layers, models
import scipy
import matplotlib.pyplot as plt


(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data() #load data keraseko datasetetik

#normalizatu dataseta
train_images, test_images = train_images/255.0, test_images/255.0

"""
Orain dataseta haundetzeko teknika bat erabiliko dugu: Irudien tamaina, forma, kokapena... aldatzea.
"""
"""
Aldaketak egiten dituen funtzioa definituko dugu hemen
"""
datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest"
)


"""
Argazki bategaz pribatuko dugu, datagen funtzioak argazki horretatik hainbat argazki eraldatuta erakutziko dizkigu
"""
test_img = train_images[1]
print(test_img.shape)
img = test_img.reshape((1,) + test_img.shape) #honekin beste dimentzio bat gehitzen diogu (lehen=(32,32), orain=(1,32,32))



i = 0
for batch in datagen.flow(img, save_prefix="test", save_format="jpeg"):
    plt.figure(i)
    plot = plt.imshow(batch[0])
    i += 1
    print(i)
    if i > 4:
        break #ez badiogu break ipintzen ez da geldituko!!
plt.show()