import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.keras.preprocessing.image import load_img, img_to_array
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

"""
Hau ez du puto azaltzen. Baina bueno egiten duen gauza bakarra datuak batchetan banatzen ditu
"""
from tensorflow.python.data.ops.dataset_ops import ShuffleDataset

BATCH_SIZE = 32
SHUFFLE_BUFFER_SIZE = 1000
train_batches = train.shuffle(SHUFFLE_BUFFER_SIZE).batch(BATCH_SIZE)
print(test)
validation_batches = validation.batch(BATCH_SIZE)
test_batches = test.batch(BATCH_SIZE)




"""
Aukeratzen pre entrenatutako modelo bat
"""
img_shape = (IMG_SIZE, IMG_SIZE, 3)

base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SIZE, 
                                               include_top=False, #classifierra ez dugu gehituko, azken kapak eskuz egingo ditugulako (DNN)
                                               weights="imagenet") #pisu desberdinak aukeratu ahal dira, gure kasuan imagenet erabiliko dugu

"""
Puntu honetan gure modeloak (32,5,5,1280) formako tensore bat itzuliko digu. Gure tensore originala (1,160,160,3) koa zen.
"""

base_model.summary()

"""
Orain freezing egingo dugu, hau da pisuak eta biases guztiak finko utziko ditugu ez aldatzekko entrenamendua egiterakoan
"""

base_model.trainable = False

"""
Oraing Pooling egingo dugu (matrixeak txikitu averagerekin), ez diogunez zenbateko matrizea adierazi 5x5 eko matrizea artuko du eta guztiari average egingo dio
"""

global_average_layer = tf.keras.layers.GlobalAveragePooling2D()

"""
Azkeneko Dense layerra gehituko dugu, bakarrik objetu bakarra asmatu behar dugunez 1 jarriko diogu
"""

prediction_layer = keras.layers.Dense(1)

"""
Orain modelo osoa batuko dugu
"""

model = tf.keras.Sequential([
    base_model,
    global_average_layer,
    prediction_layer
])

"""
Entrenamendua egitera goaz
"""

base_learning_rate = 0.0001 #tipiko alfa definitzen duena buelta bakoitzean zenbat aldatuko diren pisuak (oso txikia jartzen dugu ia dena entrenatuta dagoelako)

model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=base_learning_rate),
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), #binary erabiltzen ari gara bakarrik bi objetuen artean klasifikatzen gabizelako
              metrics = ["accuracy"])

history = model.fit(train_batches,
                    epochs=3, 
                    validation_data=validation_batches)
acc =  history.history["accuracy"]

"""
Modeloa gordetzeko!!!!
"""

model.save("dogs_vs_cats.h5") #amaiera hori keras modeloetarako berezia da

"""
Hau nire programazioaren parte da. Helburua: Edozein argazki sartu ahal izatea gure modeloak asmatu dezan. Ahal bada visualera pasatu
"""

new_model = tf.keras.models.load_model("dogs_vs_cats.h5")
prediction = new_model.predict(test_batches)

# Carga la imagen desde el disco
img = load_img('gato_fumon.jpeg', target_size=(160, 160))
# Convierte la imagen en un tensor
img_tensor = img_to_array(img)
#aurretik sortu dugun funtzioa aplikatzen
img_tensor = format_example(img_tensor, 0)
print(type(img_tensor[0]))


# Agrega una dimensión adicional para representar el tamaño del batch
img_ten = tf.expand_dims(img_tensor[0], axis=0)
# img_tensor = img_tensor.map(format_example)
print(img_ten.shape)

predict = new_model.predict(img_ten)
print(predict)