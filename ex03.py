def take(k, xs):

    return [x for i, x in enumerate(xs) if i < k]

def drop(k, xs):

    return [x for i, x in enumerate(xs) if i >= k]

def head(xs):

    return xs[0]

def tail(xs):

    return xs[1:]

def last(xs): 

    return xs[len(xs)-1]

def init(xs):

    return xs[:-1]