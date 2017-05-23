from functools import reduce

# Funções gerais

def soma(a, b):

    return a + b

def soma_pontas(p):

    return p[0] + p[1]

def soma_pt(pt):

    if len(pt) == 1:

        return pt[0]

    else: 

        return pt[0] + pt[1]

def retorna_pedras_ponta(a, m):

    return [p for p in m if a == p[0] or a == p[1]]

def count_iguais_a(px, mx):

    if type(mx) is list:

        return [pedra_igual_p(px, pd) for pd in mx].count(True)
    
    else: 

        return [px == pt for pt in mx].count(True)

def tem_duplicidades(mx):

    if type(mx) is list:

        return not [count_iguais_a(px, mx) - 1 for px in mx if count_iguais_a(px, mx) - 1] == []

    else:

        return not [count_iguais_a(cx, mx) - 1 for cx in mx if count_iguais_a(cx, mx) - 1 > 0 and len(cx) == 2] == []

def tem_invalidos(mx):

    if type(mx) is list:

        return len([pd for pd in mx if not pedrap(pd)]) > 0

    else: 

        return len([pt for pt in mx if not pontap(pt)]) > 0

def pontap(pt):

    if len(pt) != 2:

        return 0 <= pt[0] <= 6

    else:

        return pedrap(pt) and carrocap(pt)

# P01:

def pedrap(p):

    return 0 <= p[0] <= 6 and 0 <= p[1] <= 6

# P02:

def maop(m):

    return not tem_invalidos(m) and not tem_duplicidades(m) and len(m) <= 7

# P03:

def carrocap(p):

    return p[0] == p[1]

# P04:

def tem_carroca_p(m):

    return len(tem_carrocas(m)) > 0

# P05:

def tem_carrocas(m):

    return [c for c in m if carrocap(c)]

# P06:

def pontos(m):

    return reduce(soma, [soma_pontas(p) for p in m])

# P07

def garagem(m):

    soma = pontos(m)

    if soma % 5 == 0:

        return soma

    else:

        return [soma - i for i in range(1, 5) if (soma - i) % 5 == 0][0]

# P08

def pedra_igual_p(p1, p2):

    return p1 == p2 or p1[0] == p2[1] and p1[1] == p2[0]

# P09

def ocorre_pedra_p(p, m):

    return [pedra_igual_p(p, px) for px in m].count(True) > 0

# P10

def ocorre_valor_p(a, m):

    return len(retorna_pedras_ponta(a, m)) > 0

# P11

def ocorre_pedra(v, m):

    return retorna_pedras_ponta(v, m)

# P12

def pedra_maior(m):

    def maiores_que(p, m):

        return [x for x in m if soma_pontas(x) > soma_pontas(p)]

    return [y for y in m if maiores_que(y, m) == []][0]

# P13

def ocorre_valor_q(v, m):

    return len(ocorre_pedra(v, m))

# P14

def ocorre_carroca_q(m):

    return len(tem_carrocas(m))

# P15

def tira_maior(m):

    return [p for p in m if not pedra_igual_p(p, pedra_maior(m))]

# P16

def tira_maior_v(v, m):

    return pedra_maior(retorna_pedras_ponta(v, m))

# P17

def mesap(ms):

    return not tem_invalidos(ms) and not tem_duplicidades(ms) and len(ms) == 4

# P18

def carroca_m_p(ms):

    return not [pt for pt in ms if len(pt) == 2] == []

# P19

def pontos_marcados(ms):

    return reduce(soma, [soma_pt(pt) for pt in ms])

# P20

def pode_jogar_p(p, ms):

    return not [pt for pt in ms if p[0] == pt[0] or p[1] == pt[0]] == []

# P21

def fn(ms):

    return [soma_pt(pt) for pt in ms]

def pot(ls):

    return reduce(soma, ls)

def marca_ponto_p(pd, ms):

    validas = [joga_pedra(pd, ms, i) for i in range(0, 4) if joga_pedra(pd, ms, i) != False]

    sn = [fn(lol) for lol in validas]

    somas = [pot(ls) for ls in sn]

    return [sl % 5 == 0 for sl in somas].count(True) > 0

# P23

def joga_pedra(pd, ms, n):

    def jogadap(pd, ms, n):

        if len(ms[n]) == 2:

            return pd != tuple(ms[n]) and (pd[0] == ms[n][0] or pd[1] == ms[n][1])

        else:
            
            return pd[0] == ms[n][0] or pd[1] == ms[n][0]

    ms = list(ms)

    if carrocap(pd) and jogadap(pd, ms, n):

        ms[n] = [pd[0], pd[1]]

        return tuple(ms)

    elif not carrocap(pd) and jogadap(pd, ms, n):

        ms[n] = [pt for pt in pd if pt != ms[n][0]]

        return tuple(ms)

    else:
        
        return False