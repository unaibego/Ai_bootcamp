import sys

def main():
    if (len(sys.argv) != 2):
        return (0)
    if (len(sys.argv) != 2):
        print("Cantidad de argumentos no valida")
        return (1)
    if not sys.argv[1].isnumeric():
        print("Tipo de argumento no valido")
        return (1)
    num = int(sys.argv[1])
    if (num == 0):
        print("I'm zero")
    elif (num % 2 == 0):
        print("I'm Even")
    else:
        print("I'm Odd")
    return (0)

if __name__ == "__main__":
    main()