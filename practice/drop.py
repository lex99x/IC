# Solução iterativa:

def drop_i(k, xs):

    depois = []

    for i in range(k, len(xs)):

        depois.append(xs[i])

    return depois

# Solução recursiva:

def iterator(k, xs, i):

    if len(xs) == 0:

        return []

    elif i > k:

        return [xs[0]] + iterator(k, xs[1:], i + 1)

    else:

        return iterator(k, xs[1:], i + 1)

def drop_r(k, xs):

    return iterator(k, xs, 0)

# Solução Ovo de Colombo:

def drop_o(k, xs):

    return xs[k:]