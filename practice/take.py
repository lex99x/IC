# Solução iterativa:

def take_i(k, xs):

    primeiros = []

    for i in range(k):

        primeiros.append(xs[i])

    return primeiros
        
# Solução recursiva:

def iterator(k, xs, i):

    if i == k:

        return []

    elif i < k:

        return [xs[0]] + iterator(k, xs[1:], i + 1)

    else:

        return iterator(k, xs[1:], i + 1)

def take_r(k, xs):

    return iterator(k, xs, 0)

# Solução Ovo de Colombo:

def take_o(k, xs):

    return xs[:k]