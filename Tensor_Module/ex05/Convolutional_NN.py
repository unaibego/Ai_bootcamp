import tensorflow as tf
import numpy as np
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data() #load data keraseko datasetetik

#normalizatu dataseta
train_images, test_images = train_images/255.0, test_images/255.0

class_names = ["airplane", "automobile", "bird", "cat", "deer", 
               "dog", "frog", "horse", "ship", "truck"]

#irudi bat ikusiko dugu
# print(np.shape(train_images))
# img_index = 1
# plt.imshow(train_images[img_index], cmap=plt.cm.binary)
# plt.xlabel(class_names[train_labels[img_index][0]])
# plt.show()

"""
Gure modeloa sortuko dugu, horretarako hainbat gauza definitu behar dira:
-Banan banan kapa desberdinak gehitu behar dira. Konbolizio kapa baten ostean Pooling egiten da datu kopurua txikitzeko
-Pooling: Max, Min edo Average izan daiteke
"""
model = models.Sequential()
model.add(layers.Conv2D(32, (3,3), activation="relu", input_shape=(32,32,3))) #filtro kantitateta = 32, filtro_shape=(3,3)
model.add(layers.MaxPooling2D((2, 2))) #2x2-ko matrize bategaz datuak txikitzen dira. 4 datuetatik txikiena aukeratu denbora guztian
model.add(layers.Conv2D(64, (3, 3), activation="relu"))#filtro kantitateta = 32, filtro_shape=(3,3)
model.add(layers.MaxPooling2D((2,2))) #berriro ere pooling
model.add(layers.Conv2D(64, (3,3), activation = "relu"))


"""
Orain aurreko CNN-ekin gure irudiaren ezaugarriak aldarrikatu ditugu, beraz DenseNN batera bidaliko dugu bertan klasifikazioa egiteko
"""

model.add(layers.Flatten()) #lehenengo aurreko kapetan matrizetan zeuden datuak dimentzio bakarreko array batera pasau
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(10))
# model.summary()

"""
Orain entrenamendua definituko dugu
"""

model.compile(optimizer="adam",
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=["accuracy"])

history = model.fit(train_images, train_labels, epochs=4, validation_data=(test_images, test_labels))
print(history)

"""
Aurreko ariketako funtzio berdinak erabiliko ditugu gure emaitzak aztertzeko
"""

def get_num():
    num = input("Select which imagen do you want to predict: ")
    while not num.isnumeric():
        num = input("Select which imagen do you want to predict: ")
    return int(num)
def predict(img_array, model):
    return model.predict(np.array([img_array]))
def plot_imagen(prediction, class_names, img_array):
    plt.figure()
    plt.imshow(img_array)
    plt.title(class_names[np.argmax(prediction)])
    plt.colorbar()
    plt.grid(False)
    plt.show()

while 1:
    num = get_num()
    img_array = test_images[num]
    prediction = predict( img_array, model)
    print(prediction)
    plot_imagen(prediction, class_names,img_array)



