import numpy as np

def simple_predict(x, theta):
    y = theta[0] + theta[1] * x
    return y

x = np.arange(1,6).reshape(-1, 1)
theta1 = np.array([[5],[0]])
theta2 = np.array([[0],[1]])

result = simple_predict(x, theta2)
print(result.__repr__())