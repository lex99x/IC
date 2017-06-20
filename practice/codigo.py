from functools import reduce

def head(ls):

    return ls[0]

def tail(ls):

    return ls[1:]

def space(a, b):

    return a + ' ' + b

def check(t, plv):

    if t[0] == plv:

        return t[1]

    else:

        return plv

def troca(t, plvs):

    if len(plvs) == 0:

        return plvs

    else:

        return [check(t, head(plvs))] + troca(t, tail(plvs))

def codigo(ts, frs):

    if len(ts) == 1:

        plvs = frs.split()

        return troca(head(ts), plvs)

    else:

        return reduce(space, troca(head(ts), codigo(tail(ts), frs)))