import sys 


def main():
    all_string = ""
    for string in sys.argv[1:]:
        all_string = all_string + string[::-1] + " "
    reverse = all_string
    reverse_case = reverse.swapcase()
    print(reverse_case)

if __name__ == "__main__":
    main()

# esto es un comentario
