from auxiliares import *

# Parte I – Bloco I

# P01:

def pedrap(pda):

    return 0 <= pda[0] <= 6 and 0 <= pda[1] <= 6

# P02:

def maop(m):

    return not contem_invalidos(m) and not contem_duplicidades(m) and len(m) <= 7

# P03:

def carrocap(pda):

    return pda[0] == pda[1]

# P04:

def tem_carroca_p(m):

    return len(tem_carrocas(m)) > 0

# P05:

def tem_carrocas(m):

    return [pda for pda in m if carrocap(pda)]

# Parte I – Bloco 2

# P06:

def pontos(m):

    return reduce(soma, [soma(p[0], p[1]) for p in m])

# P07

def garagem(m):

    if pontos(m) % 5 == 0:

        return pontos(m)

    else:

        return [pontos(m) - n for n in range(1, 5) if (pontos(m) - n) % 5 == 0][0]

# P08

def pedra_igual_p(pda1, pda2):

    return pda1 == pda2 or pda1[0] == pda2[1] and pda1[1] == pda2[0]

# P09

def ocorre_pedra_p(pda, m):

    return len([pdax for pdax in m if pedra_igual_p(pdax, pda)]) > 0

# P10

def ocorre_valor_p(pta, m):

    return len(pdas_para_pta(pta, m)) > 0

# P11

def ocorre_pedra(pta, m):

    return pdas_para_pta(pta, m)

# P12

def pedra_maior(m):

    return maior(m)

# P13

def ocorre_valor_q(pta, m):

    return len(ocorre_pedra(pta, m))

# P14

def ocorre_carroca_q(m):

    return len(tem_carrocas(m))

# P15

def tira_maior(m):

    return [pda for pda in m if not pedra_igual_p(pda, pedra_maior(m))]

# P16

def tira_maior_v(pta, m):

    return pedra_maior(pdas_para_pta(pta, m))

# Parte I – Bloco 3

# P17

def mesap(msa):

    return not contem_invalidos(msa) and not contem_duplicidades(msa) and len(msa) == 4

# P18

def carroca_m_p(msa):

    return len([pta for pta in msa if len(pta) == 2 and carrocap(pta)]) > 0

# P19

def pontos_marcados(msa):

    if multiplo_de_cinco(soma_msa(msa)):

        return soma_msa(msa)

    else:

        return 0

# P20

def pode_jogar_p(pda, msa):

    return len(ptas_para_pda(pda, msa)) > 0

# Daqui pra frente o negócio fica tenso

# P21

def fn(ms):

    return [soma_pta(pt) for pt in ms]

def pot(ls):

    return reduce(soma, ls)

def marca_ponto_p(pd, ms):

    validas = [joga_pedra(pd, ms, i) for i in range(0, 4) if joga_pedra(pd, ms, i) != False]

    sn = [fn(lol) for lol in validas]

    somas = [pot(ls) for ls in sn]

    return [sl % 5 == 0 for sl in somas].count(True) > 0

# P22

def possiveis_mesas(pd, ms):

    return [(n, joga_pedra(pd, ms, n)) for n in range(0, len(ms)) if joga_pedra(pd, ms, n) != False]

def ponta_pontos(pd, ms):
	
	return [(possiveis_mesas(pd, ms)[i][0], pontos_marcados(possiveis_mesas(pd, ms)[i][1])) for i in range(0, len(possiveis_mesas(pd, ms))) if pontos_marcados(possiveis_mesas(pd, ms)[i][1]) != 0]	

def maior_ponto(pd, ms):

    if len(ponta_pontos) == 0:

        return "A pedra não marca pontos na mesa"

    else:

        return [ponta_pontos(pd, ms)[i][0] for i in range(0, 4) if ponta_pontos(pd, ms)[i][1] == maior([tp[1] for tp in ponta_pontos(pd, ms)])][0]
    
# P23

def joga_pedra(pd, ms, n):

    # if pode_jogar_p(pd, ms):



    ms = list(ms)

    if carrocap(pd) and jogadap(pd, ms, n):

        ms[n] = [pd[0], pd[1]]

        return tuple(ms)

    elif not carrocap(pd) and jogadap(pd, ms, n):

        ms[n] = [pt for pt in pd if pt != ms[n][0]]

        return tuple(ms)

    else:
        
        return False



def jogadap(pd, ms, n):

    if len(ms[n]) == 2:

        return pd != tuple(ms[n]) and (pd[0] == ms[n][0] or pd[1] == ms[n][1])

    else:
        
        return pd[0] == ms[n][0] or pd[1] == ms[n][0]

# P24

def jogap(m, ms):

    pds = []

    for pd in m:

        for n in list(range(0, len(ms))):

            if jogadap(pd, ms, n):

                pds.append(pd)

    return len(pds) > 0

def n_pd(pd, m):

    return [n for n, pdx in enumerate(m) if pdx == pd][0]

def n_pta_maior_pontuacao(pd, ms):

    if ponta_pontos(pd, ms) != []:

        return [ptax_ptox[0] for ptax_ptox in ponta_pontos(pd, ms) if ptax_ptox[1] == maior([pta_pto[1] for pta_pto in ponta_pontos(pd, ms)])][0]

    else:

        return False

def jogada(m, ms):

	return [(n_pd(pdx, m), n_pta_maior_pontuacao(pdx, ms)) for pdx in m if type(n_pta_maior_pontuacao(pdx, ms)) != bool]