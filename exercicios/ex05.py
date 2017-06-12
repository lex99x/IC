def head(xs):

    return xs[0]

def tail(xs):

    return xs[1:]

def ocorre(x, xs):

    return len([y for y in xs if y == x]) > 0

def norep(xs):

    if len(xs) == 0:

        return xs

    elif not ocorre(head(xs), tail(xs)):

        return [head(xs)] + norep(tail(xs))

    else:

        return norep(tail(xs))
