import sys
import tensorflow as tf
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

save_stdout = sys.stdout
sys.stdout = open("output.log", "w") #esta mierda no vale pa nada

csv_column_names = ["SepalLength", "SepalWidth", "PetalWidth", "PetalLength", "Species"]
species = ["Setosa", "Versicolor", "Virginica"]
train = pd.read_csv("iris_training.csv", names = csv_column_names, header=0)
test = pd.read_csv("iris_test.csv", names = csv_column_names, header = 0)
y_train = train.pop("Species")
y_test = test.pop("Species")



"""
Oraingoan input functiona pixkat desberdina izango da,
oraingoan lamda erabiliko dugu funtzio bakoitza sortzeko, bakoitza bere sarrerekin.
"""
def input_fn(features, labels, training=True, batch_size=256):
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle and repeat if you are in training mode.
    if training:
        dataset = dataset.shuffle(1000).repeat()

    return dataset.batch(batch_size)


my_feature_columns = []
for key in train.keys():
    my_feature_columns.append(tf.feature_column.numeric_column(key=key))


classifier = tf.estimator.DNNClassifier(feature_columns=my_feature_columns, hidden_units=[30, 10], n_classes=3)
classifier.train(input_fn=lambda: input_fn(train, y_train, training=True),steps=5000)


sys.stdout = save_stdout
eval_result = classifier.evaluate(input_fn=lambda: input_fn(test, y_test, training=False))
print("\nTest set accuracy: {accuracy:0.3}\n".format(**eval_result))

# result = list(classifier.predict(input_fn=lambda: input_fn(test, y_test, training=False)))
# print(result[0]["probabilities"]) 


"""
Orain gure sarrera propioak sartuko ditugu gure sarera
"""

def input_fn(features, batch_size=256):
    return tf.data.Dataset.from_tensor_slices(dict(features)).batch(batch_size) #beti egiten dugun sarrera funtzioa baina askoz sinpleagoa oraingoan

features = ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]
predict = {}

print("Please type numeric values as prompted.")
for feature in features:
    valid = True
    while valid:
        val = input(feature + ": ")
        if not val.isdigit():
            valid = False
        predict[feature] = [float(val)]

predictions = classifier.predict(input_fn=lambda : input_fn(predict))
for pred_dict in predictions:
    class_id = pred_dict["class_ids"][0]
    probability = pred_dict["probabilities"][class_id]
    print(f"predictions is {species[class_id]} : {probability} eta hauek guztiak dira", pred_dict["probabilities"])