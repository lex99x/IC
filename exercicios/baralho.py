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

    if m == []:

        return m

    elif head(m)[0] == n:

        return [head(m)[1]] + valores(n, tail(m))

    else:

        return valores(n, tail(m))

def cartas(n, vs):

    if vs == []:

        return vs

    else:

        return [(n, head(vs))] + cartas(n, tail(vs))


def iguais(k, ls):

    if ls == []:

        return ls

    elif head(ls) == k:

        return [head(ls)] + iguais(k, tail(ls))

    else:

        return iguais(k, tail(ls))

def nao_ocorrem(xs, ls):

    if xs == []:

        return xs

    elif iguais(head(xs), ls) == []:

        return [head(xs)] + nao_ocorrem(tail(xs), ls)

    else:

        return nao_ocorrem(tail(xs), ls)

def ocorre_seq(xs):

    if len(xs) == 1:

        return True

    elif head(xs) + 1 == head(tail(xs)):

        return ocorre_seq(tail(xs))

    else:

        return False

def ocorre_seq2(xs):

    return head(xs) == 1 and xs[len(xs) - 1] == 13

def maiores(k, ls):

    if ls == []:

        return ls

    elif len(head(ls)) > len(k):

        return [head(ls)] + maiores(k, tail(ls))


    else:

        return maiores(k, tail(ls))

def maior_len(ls):

    if ls == []:

        return len(ls)

    elif maiores(head(ls), tail(ls)) == []:

        return len(head(ls))

    else:

        return maior_len(tail(ls))

def sequencias(m, ns):

    if ns == []:

        return ns

    elif len(valores(head(ns), m)) and (ocorre_seq(ordena(valores(head(ns), m))) or ocorre_seq2(ordena(valores(head(ns), m)))):

        return [ordena(valores(head(ns), m))] + sequencias(m, tail(ns))

    else:

        return sequencias(m, tail(ns))

ns = ['c', 'e', 'o', 'p']

# 1:

def arruma(m):

    def arruma_ns(m, ns):

        if ns == []:

            return ns

        else:

            return cartas(head(ns), ordena(valores(head(ns), m))) + arruma_ns(m, tail(ns))

    return arruma_ns(m, ns)

# 2:

def completa_seq(m, n):

    vs = ordena(valores(n, m))

    if vs:

        return nao_ocorrem(list(range(head(vs), vs[len(vs) - 1])), vs)

    else:

        return vs

# 3:

def maiorseq(m):

    return maior_len(sequencias(m, ns))

# Questão bônus (opcional):

def maiorseq2(m):

    return maiorseq(m)