import random

def shuffle(split_text):
    randomlist = []
    randomlist = random.sample(range(0, len(split_text)), len(split_text))
    mylist = [split_text[i] for i in randomlist]
    return mylist

def unique(split_text):
    for i in split_text:
        if split_text.count(i) > 1:
            split_text.remove(i)
    return split_text

def generator(text, sep=" ", option="ordered"):
    if not text.isprintable():
        print("The text is not printable")
        exit()
    split_text = text.split(sep)
    if option == "shuffle":
        split_text = shuffle(split_text)
    if option == "unique":
        split_text = unique(split_text)
    if option == "ordered":
        split_text = sorted(split_text)
    for word in split_text:
        yield word
a_ver = generator ("A de alpha hola  dfa q tal guapo hola")
for i in a_ver:
    print (i)