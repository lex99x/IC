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

# P21

def marca_ponto_p(pda, msa):

    return len([pontuacao_de_pda_em_pontas[1] for pontuacao_de_pda_em_pontas in pontuacoes_de_pda_em_pontas(pda, msa) if pontuacao_de_pda_em_pontas[1] != 0]) > 0

# P22

def maior_ponto(pda, msa):

    pontuacoes = [pontuacao_de_pda_em_pontas[1] for pontuacao_de_pda_em_pontas in pontuacoes_de_pda_em_pontas(pda, msa)]

    if pontuacoes != []:

        maior_pontuacao = maior(pontuacoes)
    
        return [pontuacao_de_pda_em_pontas[0] for pontuacao_de_pda_em_pontas in pontuacoes_de_pda_em_pontas(pda, msa) if pontuacao_de_pda_em_pontas[1] == maior_pontuacao][0]

    # else:

    #     return False

# P23

def joga_pedra(pda, msa, n):

    msa = list(msa)

    msa[n] = [pta for pta in pda if pta != msa[n][0] or carrocap(pda)]

    return tuple(msa)

# P24

def jogap(m, msa):

    return len(ns_para_m(m, msa)) > 0

# P25

def jogada(m, msa):

    indices = indices_maiores_pontuacoes(m, msa)

    maior_pontuacao = maior([soma_msa(mesa_por_indice(indice, m, msa)) for indice in indices])

    return [indice for indice in indices if soma_msa(mesa_por_indice(indice, m, msa)) == maior_pontuacao]

# P26

def faz_jogada(m, msa):

    return [mesa_por_indice(indice, m, msa) for indice in jogada(m, msa)]

# Parte I – Bloco 4

# P27

def lista_de_jogadas(ljg):

    return pedrap(ljg[0]) and 
