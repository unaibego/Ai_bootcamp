def check(func):
    def inside(a, b):
        if b==0:
            print("Cant divide by 0")
            return "pelele"
        func(a, b) # hasieran konprobaketa egiten du eta gero originalki definitutako funtzioa
    return inside # logikamente funtzio berria itzultzen digu

def div(a, b):
    return a / b

div = check(div) #basikamente hemen div eraldatu du check-en dagoena egiteko

print(div(10 , 0))