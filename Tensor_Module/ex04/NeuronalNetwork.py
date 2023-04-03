import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

fashion_mnist = keras.datasets.fashion_mnist #dataseta deskargatuko dugu keras-etik, bertan ikasteko datasetak dituelako
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data() #hemen datasetetik entrenamendu eta test irudi eta etiketak lortzen ari gara

"""
Dataseta ikertzen:
"""
# print(train_images.shape) #emaitza:(60000, 28, 28)-->28x28pxl eko 60000 irudi ditugu
# print(type(train_images)) #tipo numpy.ndarraya, oso tipikoa
# print(train_images[0,23,23])#0. argazkian 23 lerro eta 23 zutabean kokatuta dagoen pixela ikusten gabiz (zenbaki bat ematen digu-->grayscale dago)
# print(train_labels[:10]) #hemen erantzunak ikusten dira zenbakiz errepresentatuta (10 label desberdin dauz)


class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt",
               "Sneaker", "Bag", "Ankle boot"]

"""
Irudi bat ikusteko
"""
# plt.figure()
# plt.imshow(train_images[2])
# plt.colorbar()
# plt.grid(False)
# plt.show()

"""
Data preprocesing:

-Lehenengo pausua: Sarrera normalizatu-->(0,1) artean ipini
    Zertarako? Gure pisuen balio randomki ezarriko da baina (0,1) arteko balioei eragin egokia izateko, 
        beste balio handiago bat sartu ezkero pisuek ez dute ia eraginik izango
 
    """
train_images = train_images/255.0
test_images = test_images/255.0

"""
Modeloa sortu:
-Zergatik sequiential? Sinpleena da, ondino ulertzen duzun bakarra (ez da konboluzionala)
-Zer doa sequentialen barruan? Pues layer bakoitza lista batean, (kerasekin sortuko ditugu layerak)
-Zer da Flatten? Basikamente matrize karratu batekin neurona lista "leun" bat sortzen du
-Zer da dense? Hidden layer egiteko balio du, aurreko kapako neurona guztiak kapa berrira konektatuta doazela zihurtatzen du.
    Lehenengo zenbat neurona jarri behar diren adierazi behar da eta ondoren ze aktibazio funtzio erabili
-Zer da relu? Aktibazio funtzio bat da (negatiboak positibo bihurtzen dituena uste dut)
-Azken kapa? Hidden kapa modura Dense erabili baina kontuz! Oraingoan neurona kop garrantsitzua da, gure modeloaren irteera kopurua izango da
"""
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")])

"""
Orain compilazioa egingo dugu:
Honekin nola entrenatuko den adieraziko diogu:
-Adam gradient decent kalkulu mota da (edo antzeko bat)
-loss ze funtzio kostu erabiliko dugun adierazten digu
-metrics da lortu nahi dugun emaitza, accuracy kasu honetan. Hau esan du baina ez dut ondo ulertzen zer den.
"""

model.compile(optimizer="adam", 
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"]) #NN batean aldatu ahal ditugun aldagaiak hyper parameters dira.

"""
Datuak sartzen gure modelora:
"""
model.fit(train_images, train_labels, epochs=1) #epoch:zenbatetan errepikatze den entrenamendua datu hoiekin. 1 ipini dut ez tardatzeko asko

"""
Orain ebaluatuko dugu beste datu batzuekin ia zelan doan
"""

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=1) #verbosek adierazi ia zer printeatzea nahi dugun--> ezebez, progres bar, single lien

print("Test accuracy", test_acc)

"""
Orain irudi bakar bat asmatuko dugu
"""

# predictions = model.predict(np.array([test_images[0]])) #lista bat izan behar da, orokorrean bat baino gehiago aztertzen delako aldi berean
# print(class_names[np.argmax(predictions)]) #predictions lista bat da probabilitate guztiekin, beraz hortik handiera hartu eta zein den ikusi
# plt.figure()
# plt.imshow(test_images[0])
# plt.colorbar()
# plt.grid(False)
# plt.show()

"""
Aurreko irudi predikzioa txukunduko dugu, lista osoko edozein irudi asmatu ahal izateko
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
    
# while 1:
#     num = get_num()
#     img_array = test_images[num]
#     prediction = predict( img_array, model)
#     print(prediction)
#     plot_imagen(prediction, class_names,img_array)

"""
Orain kanpoko zenbaki batekin probatuko dut: no va, es una mierda
"""
# rbg_array = mpimg.imread("Totebag.jpg")
# gray_scale = rbg_array.dot(np.array([0.114, 0.587, 0.299]))
# gray_scale = 1 - gray_scale
# print(gray_scale.shape)
# prediction = predict( gray_scale, model)
# print(prediction)
# plot_imagen(prediction, class_names,gray_scale)