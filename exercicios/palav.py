def head(p):

    return p[0]

def tail(p):

    return p[1:]

def num(c):

    if 48 <= ord(c) <= 57:

        return int(c)

    else:

        return c

def e_palav(p):

    ps = list(p)

    if len(ps) == 0:

        return False

    elif type(num(head(ps))) is int:

        return True

    else: 

        return e_palav(tail(ps))