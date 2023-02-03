import sys
def main(a, b):
    if not a.isnumeric() or not b.isnumeric():
        print("Los argumentos no son numericos")
        return 0
    print("Sum:         ", int(a)+int(b))
    print("Difference:  ", int(a)-int(b))
    print("Product:     ", int(a)*int(b))
    try:
        print("Quotient:    ", int(a)/int(b))
    except:
            print("Quotient: Algo has metido mal")
    try:
        print("Remainder:   ", int(a)%int(b))
    except:
            print("Remainder: Algo has metido mal")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Cantidad de argumentos no valida")
    else:
        main(sys.argv[1], sys.argv[2])