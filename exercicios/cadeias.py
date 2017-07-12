# P40: Verificar se uma cadeia é uma palavra (apenas letras). e_palav(cadeia)

def letra(c): return 'A' <= c <= 'Z' or 'a' <= c <= 'z'

def e_palav(cs):

    if len(cs) == 0: return True

    elif not letra(cs[0]): return False

    else: return e_palav(cs[1:])

# P41: Verificar se uma cadeia é um número inteiro positivo. e_int(cadeia)

def num(c): return '0' <= c <= '9'

def e_int(cs):

    if len(cs) == 0: return True

    elif not num(cs[0]): return False

    else: return e_int(cs[1:])

# P42: Dado um verbo regular e um tempo do modo indicativo, produzir as conjugações. conjuga(verbo,tempo)

def conjuga_ds(v, ps, ds):

    if ds == ():

        return []

    else:

        return [ps[0] + ' ' + v[:-2] + ds[0]] + conjuga_ds(v, ps[1:], ds[1:])

def conjuga_t(v, t, ps, ts):

    if ts[0][0] == t:

        return conjuga_ds(v, ps, ts[0][1])

    else:

        return conjuga_t(v, t, ps, ts[1:])

def conjuga(v, t):

    ps = ('eu', 'tu', 'ele', 'nós', 'vois', 'eles')
    
    ts = (
        
        ('preterito', ('ei', 'aste', 'ou', 'amos', 'astes', 'aram')), 
        ('presente', ('o', 'as', 'a', 'amos', 'ais', 'am')),
        ('futuro', ('arei', 'arás', 'ará', 'aremos', 'areis', 'atarão'))
        
    )

    return conjuga_t(v, t, ps, ts)