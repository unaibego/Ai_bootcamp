
class Vector:
    def __add__(self, add_vector):
        index = 0
        new_vector = []
        if len(self.vector) > 1: 
            for i in self.vector:
                new_vector.append([self.vector[index] + add_vector.vector[index]]) 
                index += 1
            return ([new_vector])
        else: 
            for i in self.vector:
                new_vector.append(self.vector[index][0] + add_vector.vector[index][0]) 
                index += 1
            return ([new_vector])

    def __init__(self, vector):
        self.vector = vector
    def __str__(self):
        return f"{self.vector}"
    def T(self):
        transpose_vector = []
        if len(self.vector) == 1:
            for value in self.vector[0]:
                transpose_vector.append([value])
            return (transpose_vector)
        else:
            for value in self.vector:
                transpose_vector.append(value[0])
            return ([transpose_vector])
    def dot(self, dot_vector):
        dot = 0
        self.vector = transpose(self.vector)
        dot_vector = transpose(dot_vector)
        if len(dot_vector[0]) != len(self.vector[0]):
            print("Enter a vector of the same shape")
            return (0)
        for i in range(len(self.vector[0])):
            dot = dot + self.vector[0][i] * dot_vector[0][i]
        return (dot)
    def shape(self):
        return len(self.vector), len(self.vector[0])


def transpose(vector):
    if len(vector) > 1:  #hemen oso kutre egin duzu, formatu ezegokian egon ezkero aldatu (funtzio bat erabiltzea egokiagoa izango litzateke)
        transpose_vector = []
        for value in vector:
            transpose_vector.append(value[0])
        return [transpose_vector]             #honarte




v1 = Vector([[1], [2], [4]])
v2 = Vector([[4], [5], [7]])
v3 = v1 + v2
print(v3)
print(v1.dot([[1], [1], [1]]))
print(v1.shape())
print(v1.T())
print(v1.T())