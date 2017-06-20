from functools import reduce

def concatenate_chars(x, y):

    return x + y

def convert_char(c):

    if c == '∙':

        return '*'

    elif c == '^':

        return '**'

    elif c == ',':

        return '.'

    else:

        return c

def calc(x):

    return eval(reduce(concatenate_chars, [convert_char(c) for c in list(x)]))