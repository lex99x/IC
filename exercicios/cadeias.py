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

def conjuga_ds_x(v, n, ps, ds_x):

    if ps == []:

        return ps

    else:

        return [ps[0] + ' ' + v[:-2] + ds_x[n][0]] + conjuga_ds_x(v, n, ps[1:], ds_x[n][1:])

def conjuga_t(v, t, ps, ds_x):

    if t == 'preterito': return conjuga_ds_x(v, 0, ps, ds_x)

    elif t == 'presente': return conjuga_ds_x(v, 1, ps, ds_x)

    elif t == 'futuro': return conjuga_ds_x(v, 2, ps, ds_x)

def conjuga(v, t):

    ps = ['eu', 'tu', 'ele', 'nós', 'vois', 'eles']

    ds_ar = [

        ['ei', 'aste', 'ou', 'amos', 'astes', 'aram'],
        ['o', 'as', 'a', 'amos', 'ais', 'am'],
        ['arei', 'arás', 'ará', 'aremos', 'areis', 'atarão']

    ]

    ds_er = [

        ['i', 'este', 'eu', 'emos', 'estes', 'eram'],
        ['o', 'es', 'e', 'emos', 'eis', 'em'],
        ['erei', 'erás', 'erá', 'eremos', 'ereis', 'erão']

    ]

    ds_ir = [

        ['i', 'iste', 'itiu', 'itimos', 'itistes', 'iram'],
        ['o', 'es', 'e', 'imos', 'is', 'em'],
        ['irei', 'irás', 'irá', 'iremos', 'ireis', 'irão']

    ]

    sfx = v[len(v) - 2:]

    if sfx == 'ar': return conjuga_t(v, t, ps, ds_ar)

    elif sfx == 'er': return conjuga_t(v, t, ps, ds_er)

    else: return conjuga_t(v, t, ps, ds_ir)