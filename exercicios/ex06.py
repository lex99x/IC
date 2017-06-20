def head(ls):

    return ls[0]

def tail(ls):

    return ls[1:]

def insord(k, xs):

    if len(xs) == 0:

        return [k]

    elif k < head(xs):

        return [k] + xs

    else:

        return [head(xs)] + insord(k, tail(xs))

def ordena(xs):

    if len(xs) == 0:

        return xs

    else:

        return insord(head(xs), ordena(tail(xs)))

def valores(n, m):

    return [v for (nx, v) in m if nx == n]

def cartas(n, vs):

    return [(n, v) for v in vs]

def ocorre(x, xs):

    return len([y for y in xs if y == x]) > 0

def ocorre_seq(xs):

    if len(xs) == 1:

        return True
    
    elif head(xs) + 1 == head(tail(xs)):

        return ocorre_seq(tail(xs))

    else:

        return False

def ocorre_maiores(l, ls):

    return [x for x in ls if len(x) > len(l)] != []

def maior_len(ls):

    return len(head([l for l in ls if not ocorre_maiores(l, ls)]))

# 1:

def arruma(m):

    return cartas('c', ordena(valores('c', m))) + cartas('e', ordena(valores('e', m))) + cartas('o', ordena(valores('o', m))) + cartas('p', ordena(valores('p', m)))

# 2:

def completa_seq(m, n):

    vs = ordena(valores(n, m))

    if vs:

        return [x for x in range(vs[0], vs[len(vs) - 1]) if not ocorre(x, vs)]

    else:

        return []

# 3:

def maiorseq(m):

    return maior_len([ordena(valores(n, m)) for n in ('c', 'e', 'o', 'p') if len(valores(n, m)) and ocorre_seq(ordena(valores(n, m)))])