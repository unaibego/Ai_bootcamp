import tensorflow as tf
string = tf.Variable("This is a string", tf.string) #zero dimentzioko (rank_0) tensore bat
rank1_tensor = tf.Variable(["Text", "ok"], tf.string) #dimentzio batekoa
# print(tf.rank(rank1_tensor))
# print(rank1_tensor.shape)
tensor1 = tf.ones([1,2,3]) #sortu tensore bat barruan lista bat duela. lista honen barruan bi lista dituena eta barruan hiru balio dituela
tensor2 = tf.reshape(tensor1, [2,3,1]) #aldatu aurreko tensorea shape honekin
tensor3 = tf.reshape(tensor1, [3, -1]) #orain -1 jarri diogu berak asmatzeko falta den balioa (kasu honetan [3,2] sortuko du)
# print(tensor1)
# print(tensor2)
# print(tensor3)
# ********************************************ariketak*******************************************************************
t = tf.zeros([5,5,5,5])
t = tf.reshape(t, [125, -1]) #basikamente lo del -1 es la polla
print(t)