import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow.compat.v2.feature_column as fc
import tensorflow as tf

df_train = pd.read_csv("train.csv")
df_eval = pd.read_csv("eval.csv")
# print(df_train)
y_train = df_train.pop("survived") #honela ateratze ditugu survived zutabea (hori gure erantzuna izango litzateke)(inputa eta outputa banatzeko)
y_eval = df_eval.pop("survived")
# print(y_train)

categorical_data = ["sex","n_siblings_spouses", "parch", "class", "deck", "embark_town", "alone"]
numerical_data = ["age", "fare"]
"""
 Basikamente, gizonak esan du categoria eta zenbakiekin "feature_column"-ak egin behar direla linear regresion sortzeko. Zer dira column hauek:
 Ba ezaugarriei balioa ematen dioten zutabeak, adb: sex=M,F izan daiteke--> berak sex=(0,1) gordetzen du jakiteko bi aldagai egon ahal direla.
 Segun chat gpt: Convierte los datos en una forma mas adecuada para el entreno de la red
"""
feature_colums = []
for feature_name in categorical_data:
    values = df_train[feature_name].unique()
    feature_colums.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, values))

for feature_name in numerical_data:
    feature_colums.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

def make_input_fn(data_df, label_df, num_epoch=10, shuffle=True, batch_size=32):  
    def input_function(): 
        ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df)) #tf.data.Dataset objetua sortzen da hemen
        print(ds)
        if shuffle:
            ds = ds.shuffle(1000) #basikamente datuak desordenatzen ditu, 1000 erabiliko duen bufferra da
        ds = ds.batch(batch_size).repeat(num_epoch) #hau 32 datuko batchetan banatuko du Dataseta (eta num_epoch aldiz errepikatu)
        return ds
    return input_function  

train_imput_fn = make_input_fn(df_train, y_train) #hemen funtzio bat sortzen gaude (input_function funtzioa) basikamente aurreko mobida dena balio du sortutako funtzioak inputik ez aukitzeko
eval_input_fn = make_input_fn(df_eval, y_eval, num_epoch = 1, shuffle = False)


save_stdout = sys.stdout  #aurreko entrenamenduko metodoak mierdak ez inprimatzeko baina ez du funtzionatzen
sys.stdout = open("output.log", "w")


linear_est = tf.estimator.LinearClassifier(feature_columns=feature_colums) #hemen erregresio linealeko modulua sortzen gabiz aurretik sortu dugun feature column erabilita

linear_est.train(train_imput_fn) #entrenatzen (sarrera moduan funtzio bat behar du datu guztiekin. Horregatik aurreko mobida dena egin dugu)
result = linear_est.evaluate(eval_input_fn) #ebaluatzeko berdina egin behar da baina honek irteera du (zein ondo entrenatu den esaten diguna)


# print(result)
# print(result["accuracy"]) #ikusten ia zenbate emaitza zuzen izan dituen ehunekotan



result = list(linear_est.predict(eval_input_fn))
sys.stdout = save_stdout
print("***************************** emaitzak ikusten ********************************")
person = 0
print(df_eval.loc[person]) #hemen gabiz ikusten pertsona baten datuak
print(y_eval.loc[person]) #hemen ia pertsona hori hil egin zen
print(result[person]["probabilities"][1]) # eta hemen gure IA-k bizirauteko kalkulatzen duen probabilitatea