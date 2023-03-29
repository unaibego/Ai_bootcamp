import numpy as np
import sys
sys.path.insert(0, "..")
from ex03.tools import add_intercept

def simple_predict(x, theta):
    X = add_intercept(x)
    y = X.dot(theta)
    return y

x = np.arange(1,6).reshape(-1, 1)
theta1 = np.array([[5],[0]])
theta2 = np.array([[0],[1]])

result = simple_predict(x, theta2)
print(result.__repr__())