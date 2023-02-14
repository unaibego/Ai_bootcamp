class Evaluator:
    #static method es para que puedas llamar a esa funcion sin crear un objeto tipo evaluator
    @staticmethod
    def zip_evaluate(lista, coef):
        if len(lista) != len(coef):
            print("The lenght of lists are different")
            return -1
        #la unica utilidad de zip aqui es que el for lo itera los dos a la vez y asi no pones contador
        # gainera jarri dudan moduan hasierakoari append egiten dio
        result = [len(i1) * i2 for i1, i2 in zip(lista, coef)] 
        return (result)
    @staticmethod
    def enumerate_evaluate(lista, coef):
        if len(lista) != len(coef):
            print("The lenght of lists are different")
            return -1
        result = [len(i2) * coef[i1] for i1, i2 in enumerate(lista)] 
        return (result)


lista = ["Unai", "Begoña", "Alvarez", "Conde"]
coef = [1, 1, 1, 1]
erantzuna1 = Evaluator.enumerate_evaluate(lista, coef)
print (erantzuna1)
erantzuna2 = Evaluator.zip_evaluate(lista, coef)
print (erantzuna2)