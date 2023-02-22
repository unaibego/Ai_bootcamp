def ft_filter(function_to_apply, iterable):
    re = []
    for x in iterable:
        if function_to_apply(x):
            re.append(x)
    return re
# def
x = [1, 2, 3]
h = ft_filter(lambda dum: not (dum % 2), x)
print(h)