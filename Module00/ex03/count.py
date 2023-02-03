import sys
def text_analyzer(string=None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    caracters = 0
    count_upper = 0
    count_lower = 0
    punctuation = 0
    space = 0
    if string == None:
        string = input("What is the text to analyze? ")
    if (not (type(string) == str)):
        print("Argument is not a string")
        return 0
    for caracter in string:
        if caracter.isupper():
            count_upper = count_upper + 1
        if caracter.islower():
            count_lower = count_lower + 1
        for punt in ['.', ':', ',', '!', '?', '¿']:
            if (caracter == punt):
                punctuation = punctuation + 1
        if caracter.isspace():
            space = space + 1
        caracters = caracters + 1
    print(f"The text contains {caracters} character(s):")
    print( count_upper, " upper letter(s)\n", count_lower, " lower letter(s)\n", punctuation, " punctuation mark(s)\n", space, " space(s)")

if __name__ == "__main__":
    if (len(sys.argv) > 2):
        print("Cantidad de argumentos invalida")
    if (len(sys.argv) == 2):
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()
