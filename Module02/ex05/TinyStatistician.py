def check(function):
    def cheking(self, *array):
        if not array or type(array[0]) != list:
            print("your array is not an array")
        else:
            return function(self, array[0])
        return None
    return cheking



class TinyStatistician():
    @check
    def __init__(self):
        pass
    @check
    def mean(self, array):
        return(sum(array)/len(array))
    @check
    def median(self, array):
        return(float(sorted(array)[len(array)//2])) #para que salga redondeado a la baja le pones dos
    @check
    def quartiles(self, array):
        return([sorted(array)[len(array)//4], sorted(array)[len(array)//4*3]])
    @check
    def var(self, array):
        return(self.mean([(x - self.mean(array))**2 for x in array]))
    @check
    def std(self, array):
        return(self.var(array)**0.5)
    
array = [1, 42, 300, 10, 59]
stadistic = TinyStatistician()
print(stadistic.mean(array))
print(stadistic.median(array))
print(stadistic.quartiles(array))
print(stadistic.var(array))
print(stadistic.std(array))
