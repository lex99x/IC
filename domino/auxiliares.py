from functools import reduce
from abstratas import *

# Notações:

# m: mão
# msa: mesa
# mx: mão OU mesa
# pda: pedra
# pta: ponta
# px: pedra OU ponta
# n: número (índice) de ponta de mesa

# Retorna soma dos lados de pta (int)

def soma_pta(pta):

    if len(pta) == 1:

        return pta[0]

    else:

        return soma(pta[0], pta[1])

# Retorna soma das pontas de msa (int)

def soma_msa(msa):

    return reduce(soma, [soma_pta(pta) for pta in msa])

# Verifica se pda contém pta, complementa a funções pdas_para_pta e pda_joga_em_pta (boolean)

def pda_contem_pta(pta, pda):

    return pda[0] == pta or pda[1] == pta

# Retorna lista de pedras em m que contém pta, complementa as funções dos problemas P10, P11 e P16 (list)

def pdas_para_pta(pta, m):

    return [pda for pda in m if pda_contem_pta(pta, pda)]

# Verifica se é válido jogar pda em pta, complementa as funções ptas_para_pda e joga_pedra (boolean)

def pda_joga_em_pta(pda, pta):

    return pda != tuple(pta) and pda_contem_pta(pta[0], pda)

# Retorna lista de números de ponta de msa que formam uma jogada válida com pda, complementa a função do problema P20 e a função msas_possiveis (list)

def ptas_para_pda(pda, msa):

    return [n for n, pta in enumerate(msa) if pda_joga_em_pta(pda, pta)]

# Retorna quantidade de elementos iguais a px em mx, complementa a função contem_duplicidades (int)

def qnt_iguais(px, mx):

    from domino import pedra_igual_p

    if type(mx) is list:

        return len([pda for pda in mx if pedra_igual_p(pda, px)])

    else:

        return len([pta for pta in mx if pta == px])

# Verifica se mx contém elementos iguais, complementa as funções maop e mesap (boolean)

def contem_duplicidades(mx):

    if type(mx) is list:

        return len([qnt_iguais(pda, mx) - 1 for pda in mx if qnt_iguais(pda, mx) - 1]) > 0

    else:

        return len([qnt_iguais(pta, mx) - 1 for pta in mx if qnt_iguais(pta, mx) - 1 and len(pta) == 2]) > 0

# Verifica se pta é uma entrada válida para ponta de mesa (boolean)

def pontap(pta):

    from domino import pedrap, carrocap

    if len(pta) != 2:

        return 0 <= pta[0] <= 6

    else:

        return pedrap(pta) and carrocap(pta)

# Verifica se mx contém elementos inválidos, complementa as funções maop e mesap (boolean)

def contem_invalidos(mx):

    from domino import pedrap

    if type(mx) is list:

        return len([pda for pda in mx if not pedrap(pda)]) > 0

    else:

        return len([pta for pta in mx if not pontap(pta)]) > 0

# Retorna lista de duplas com a enésima ponta de msa e a combinação de pda em msa na ponta n, respectivamente, complementa a função pontos_pda_em_msa (list)

def combinacoes_possiveis(pda, msa):

    from domino import joga_pedra, mesap

    return [(n, joga_pedra(pda, msa, n)) for n in ptas_para_pda(pda, msa) if mesap(joga_pedra(pda, msa, n))]

# Retorna lista de duplas com a enésima ponta de msa e a pontuação da combinação de pda em msa na ponta n, respectivamente, complementa as funções dos problema P21 e P22 (list)

def pontuacoes_de_pda_em_pontas(pda, msa):

    from domino import pontos_marcados

    return [(combinacao_possivel[0], pontos_marcados(combinacao_possivel[1])) for combinacao_possivel in combinacoes_possiveis(pda, msa)]

# Retorna lista de duplas com a enésima pedra em m e sua lista de números de ponta que formam uma jogada válida em msa, respectivamente, complementa a função do problema P22 (list)

def ns_para_m(m, msa):

    return [(pda, ptas_para_pda(pda, msa)) for pda in m if ptas_para_pda(pda, msa) != []]

# Retorna o número (índice) de pda em m, complementa a função gerar_indices (int)

def n_de_pda_em_m(pda, m):

    return [n for n, pdax in enumerate(m) if pdax == pda][0]

# Retorna lista de índices com as maiores pontuações das pedras de m em msa (list)

def indices_maiores_pontuacoes(m, msa):

    from domino import maior_ponto

    return [(n_de_pda_em_m(pda, m), maior_ponto(pda, msa)) for pda in m if maior_ponto(pda, msa) != None]

# Retorna tupla com nova mesa gerada a partir dos índices e demais valores informados (tuple)

def mesa_por_indice(indice, m, msa):

    from domino import joga_pedra

    return joga_pedra(m[indice[0]], msa, indice[1])

# Verifica se ldj contém sequencia de pedras em pontas erradas

def sequencias_em_pontas_erradas(ldj):

    return ldj[2] != [] and ldj[4] != []
