import tensorflow as tf
import pandas as pd

csv_column_names = ["SepalLength", "SepalWidth", "PetalWidth", "PetalLength", "Species"]
species = ["Setosa", "Versicolor", "Virginica"]

train = pd.read_csv("iris_training.csv", names = csv_column_names, header=0)
test = pd.read_csv("iris_test.csv", names = csv_column_names, header = 0)
# print(t rain.head())
y_train = train.pop("Species")
y_test = test.pop("Species")
# print(train.shape)


"""
Oraingoan input functiona pixkat desberdina izango da, 
oraingoan lamda erabiliko dugu funtzio bakoitza sortzeko, bakoitza bere sarrerekin.
"""

def input_fn(features, labels, training=True, batch_size=256):
    dataset = tf.data.Dataset.from_tensor_slices(dict(features), labels)
    if training:
        dataset.shuffle(1000).repeat()

    return dataset.batch(batch_size)

my_feature_columns = []

for key in train.keys():
    my_feature_columns.append(tf.feature_column.numeric_column(key=key))


classifier = tf.estimator.DNNClassifier(feature_columns = my_feature_columns, hidden_units=[30,10], n_classes=3)
classifier.train(input_fn=lambda : input_fn(train, y_train, training=True), steps = 5000)