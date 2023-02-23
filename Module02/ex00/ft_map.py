def ft_map(function_to_apply, iterable):
    return ([function_to_apply(x) for x in iterable])
# def
x = [1, 2, 3, 4, 5]
h = ft_map(lambda dum: dum + 1, x)
print(h)