# 1:

def pa(xs):

    if len(xs) <= 2: return False

    elif len(xs) == 3: return (xs[1] - xs[0]) + xs[1] == xs[2]

    else: return (xs[1] - xs[0]) + xs[1] == xs[2] and pa(xs[1:])

# 2:

def placa(xs):

    if len(xs) == 8: return 'A' <= xs[0] <= 'P' and placa(xs[1:])

    elif 6 <= len(xs) <= 7: return 'A' <= xs[0] <= 'Z' and placa(xs[1:])

    elif len(xs) == 5: return xs[0] == ' ' and placa(xs[1:])

    elif 2 <= len(xs) <= 4: return '0' <= xs[0] <= '9' and placa(xs[1:])

    elif len(xs) == 1: return '0' <= xs[0] <= '9'

    else: return False

# 3:

def freq(k, xs):

    if len(xs) == 0: return 0

    elif k == xs[0]: return 1 + freq(k, xs[1:])

    else: return freq(k, xs[1:])

def permuta_c(xs, ys, xsc):

    if len(xsc) != len(ys): return False

    elif len(xs) == 1: return freq(xs[0], xsc) == freq(xs[0], ys)

    else: return freq(xs[0], xsc) == freq(xs[0], ys) and permuta_c(xs[1:], ys, xsc)

def permuta(xs, ys): return permuta_c(xs, ys, xs)

# 4:

def vals(n, m):

    if m == []: return m

    elif m[0][0] == n: return [m[0][1]] + vals(n, m[1:])

    else: return vals(n, m[1:])

def nao_ocorrem(xs, ys):

    if len(xs) == 0: return xs

    elif xs[0] not in ys: return [xs[0]] + nao_ocorrem(xs[1:], ys)

    else: return nao_ocorrem(xs[1:], ys)

def completa_seq(m, n):

    vals = vals(n, m)

    if len(vals) >= 2: return nao_ocorrem(list(range(vals[0], vals[len(vals) - 1])), vals)

    else: return []

# 5:

def insord(k, xs):

    if len(xs) == 0: return [k]

    elif k < xs[0]: return [k] + xs

    else: return [xs[0]] + insord(k, xs[1:])

def ordena(xs):

    if len(xs) == 0: return xs

    else: return insord(xs[0], ordena(xs[1:]))

def maiores_len(k, xs): return [x for x in xs if len(x) > len(k)]

def maior_len(xs): return len([x for x in xs if maiores_len(x, xs) == []][0])

def ocorre_seq(vals): 
    
    vals = ordena(vals)

    return len(vals) >= 2 and (pa(vals) or (vals[0] == 1 and vals[len(vals) - 1] == 13))

ns = ['c', 'e', 'o', 'p']

def sequencias(ns, m): return [vals(n, m) for n in ns if ocorre_seq(vals(n, m))]

def maiorseq(m): return maior_len(sequencias(ns, m))