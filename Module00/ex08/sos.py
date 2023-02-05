import sys

morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'Ñ':'--.--', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'}

def change_morse(string):
    for char in string:
        print(morse.get(char, "/"), end="")
        

if __name__ == "__main__":
    lista = sys.argv[1:]
    string = ' '.join(lista)
    for char in string:
        if not char.isupper() and char != " ":
            print("Error")
            exit (0)
    change_morse(string)