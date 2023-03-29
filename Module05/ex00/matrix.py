def decorador(function):
    def check_shape(self, matrix):
        if len(self.data) != len(matrix.data):
            raise Exception("Try with matrix of the same shape")
        for i in range(len(self.data)):
            if len(self.data[i]) != len(matrix.data[i]):
                raise Exception("JopeTry with matrix of the same shape")
        return function(self, matrix)
    return check_shape 

class Matrix():
    def __init__(self, input):
        # if all(type(element) == list for element in kwargs): Azkenean ez dut behat baina hemen utziko dut interesgarria delako
        if type(input) == list:
            self.data = input
        elif type(input) == tuple:
            self.data = []
            row = []
            for i in range(input[1]):
                row.append(0)
            for i in range(input[0]):
                self.data.append(row)
        else:
            raise Exception("Please enter a correct data")
        if isinstance(self.data[0], list):
            self.shape = (len(self.data), len(self.data[0]))
        else:
            self.shape = (len(self.data))
    @decorador
    def __add__(self, add_matrix):
        new_matrix = []
        for i in range(len(self.data)):
            new_matrix.append([])
            for j in range(len(self.data[i])):
                new_matrix[i].append(self.data[i][j] + add_matrix.data[i][j])
        return (Matrix(new_matrix))
    def __radd__(self, number):
        new_matrix = []
        for i in range(len(self.data)):
            new_matrix.append([])
            for j in range(len(self.data[i])):
                new_matrix[i].append(self.data[i][j] + number) 
        return (Matrix(new_matrix))
    @decorador
    def __sub__(self, add_matrix):
        new_matrix = []
        for i in range(len(self.data)):
            new_matrix.append([])
            for j in range(len(self.data[i])):
                new_matrix[i].append(self.data[i][j] - add_matrix.data[i][j])
        return (Matrix(new_matrix))
    def __rsub__(self, number):
        new_matrix = []
        for i in range(len(self.data)):
            new_matrix.append([])
            for j in range(len(self.data[i])):
                new_matrix[i].append(self.data[i][j] - number) 
        return (Matrix(new_matrix))
    def __truediv__(self, number):
        new_matrix = []
        for i in range(len(self.data)):
            new_matrix.append([])
            for j in range(len(self.data[i])):
                new_matrix[i].append(self.data[i][j] / number) 
        return (Matrix(new_matrix))
    def __mul__(self, number):
        new_matrix = []
        for i in range(len(self.data)):
            new_matrix.append([])
            for j in range(len(self.data[i])):
                new_matrix[i].append(self.data[i][j] * number) 
        return (Matrix(new_matrix))
    def __str__(self):
        string = f"Matrix({self.data})"
        return string
    def T(self):
        new_matrix = []
        for i in range(len(self.data)):
            new_matrix.append([])
            for j in range(len(self.data[i])):
                new_matrix[i].append(self.data[j][i])
        return (Matrix(new_matrix))
class Vector(Matrix):
    def dot(self):
        return self.T()


    
    
