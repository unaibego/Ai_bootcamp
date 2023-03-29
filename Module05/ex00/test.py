from matrix import Matrix
from matrix import Vector

m1 = Matrix((2,3))
print(m1.shape)
# m1 = Matrix([[1,2,3], [4,5,6], [7,8,9]])
m2 = Matrix([1,2,3])
m3 = m2.T()
m4 = m2 * 2
print(m3)
v1 = Vector([1, 2, 3])
# print(v1.dot())

