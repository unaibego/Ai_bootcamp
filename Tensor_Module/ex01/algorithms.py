from __future__ import absolute_import, division, print_function, unicode_literals

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