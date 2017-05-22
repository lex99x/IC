from functools import reduce

# Funções gerais

def soma(a, b):

    return a + b

def soma_pontas(p):

    return p[0]+p[1]

def retorna_pedras_ponta(a, m):

    return [p for p in m if a == p[0] or a == p[1]]

# P01:

def pedrap(p):

    return 0 <= p[0] <= 6  and 0 <= p[1] <=6

# P02:

def maop(m):

    def invalidos(m):

        return [p for p in m if not pedrap(p)]

    def count_iguais_a(p, m):

        return [pedra_igual_p(p, px) for px in m].count(True)

    def verificar_duplicidade(m):

        return reduce(soma, [count_iguais_a(px, m) - 1 for px in m]) > 0

    return invalidos(m) == [] and not verificar_duplicidade(m) and len(m) <= 7

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

    def pontap(pt):

        if len(pt) != 2:

            return 0 <= pt[0] <= 6

        else:

            return pedrap(pt) and carrocap(pt)

    def carrocas_iguais(ms):

        return []

    return [pt for pt in ms if not pontap(pt)] == [] and len(ms) == 4

# P18

def carroca_m_p(ms):

    return not [pt for pt in ms if len(pt) == 2] == []

# P19

def pontos_marcados(ms):

    def soma_pt(pt):

        if len(pt) == 1:

            return pt[0]

        else: 

            return pt[0]+pt[1]

    return reduce(soma, [soma_pt(pt) for pt in ms])

# P20

def pode_jogar_p(p, ms):

    return not [pt for pt in ms if p[0] == pt[0] or p[1] == pt[0]] == []

# P21

# def marca_ponto_p(p, ms):