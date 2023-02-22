def ft_map(function_to_apply, iterable):
    re = []
    for x in iterable:
        re.append(function_to_apply(x))
    return (re)
# def
x = [1, 2, 3, 4, 5]
h = ft_map(lambda dum: dum + 1, x)
print(h)