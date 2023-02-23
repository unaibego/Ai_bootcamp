def ft_reduce(function_to_apply, iterable):
    string = ""
    try:
        for x in reversed(iterable):
            string = function_to_apply(x,string)
        return string
    except:
        return None
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
# ... Your code here ...
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
