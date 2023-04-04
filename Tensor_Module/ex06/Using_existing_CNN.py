import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_datasets as tfds
keras = tf.keras

"""
Hemen datuak deskargatzen dira modu berezi batean.
Cats_vs_dog dataseta deskargatzen du baina 3 zatitan banatzeko eskatzen dio: %80==train, %10==test eta %10==validation
"""

(raw_train, raw_validation, raw_test), metadata = tfds.load(
    "cats_vs_dogs",
    split=["train[:80%]", "train[80%:90%]", "train[90%:]"],
    with_info=True,
    as_supervised=True
)

#hemen libreriatik funtzio bat hartzen du indizetik etiketa lortzen duena
get_label_name = metadata.features["label"].int2str

#sin mas bi irudi printeatzeko
for image, label in raw_train.take(2):
    plt.figure()
    plt.imshow(image)
    plt.title(get_label_name(label))


"""
Irudiek tamaina desberdina dute beraz reshape egin behar diegu
"""

IMG_SIZE =160 #azaltzen du hobea dela irudiak txikitzea handitzea baino

def format_example(image, label):
    image = tf.cast(image, tf.float32) #imageko aldagai guztiak floatera pasatu (int-ak egon ahal dira)
    image = (image/127.5) - 1 #kasu honetan irteera [-1,1] artean egotea nahi dugu
    image = tf.image.resize(image,(IMG_SIZE, IMG_SIZE)) #funtzio honek shape berri bat ematen die irudiei
    return image, label

"""
Hemen irudi guztiei aurreko funtzioa aplikatzen diogu
"""
train =raw_train.map(format_example) #map-ek raw_traineko aldagai guztiak artu eta funtzio hori aplikatzen die
validation = raw_validation.map(format_example)
test = raw_test.map(format_example)


"""
Berriro ere inprimatzen aldaketa ikusteko
"""
for image, label in train.take(2):
    plt.figure()
    plt.imshow(image)
    plt.title(get_label_name(label))


