from functools import reduce
from abstratas import *

# Notações:

# m: mão
# msa: mesa
# mx: mão OU mesa
# pda: pedra
# pta: ponta
# px: pedra OU ponta

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

# Verifica se é válido jogar pda em pta, complementa a função ptas_para_pda (boolean)

def pda_joga_em_pta(pda, pta):

    return pda != tuple(pta) and pda_contem_pta(pta[0], pda)

# Retorna lista de pontas em ms que forma uma jogada válida com pda, complementa a função do problema P20 (list)

def ptas_para_pda(pda, msa):

    return [pta for pta in msa if pda_joga_em_pta(pda, pta)]

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