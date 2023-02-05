import sys

def ft_filter(n, s):
    if not n.isnumeric() or type(s) != str:
        print("2.Error")
        return 0
    for caracter in [",", ".", ":", ";", "!", "?", "¿"]:
        s = s.replace(caracter, "")
    string = s.split(" ")
    string_removed = s.split(" ")
    for word in string:
        if len(word) <= int(n):
            string_removed.remove(word)
    print(string_removed)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("1.Error")
    else:
        ft_filter(sys.argv[2], sys.argv[1])


