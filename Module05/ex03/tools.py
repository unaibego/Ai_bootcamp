import numpy as np
def add_intercept(x):
    colum = np.ones((np.shape(x)[0], 1))
    return np.concatenate([colum, x], axis = 1)

y = np.arange(1,10).reshape((3,3))
add_intercept(y)

# print(add_intercept(y))