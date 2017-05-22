# Funcões globais/gerais

def soma(a, b):

    return a + b

def soma_pontas(p):

    return p[0]+p[1]

def retorna_pedras_ponta(a, m):

    return [p for p in m if a == p[0] or a == p[1]]

def pontap(pt):

    if len(pt) == 2:

        return pedrap(pt) and carrocap(pt)

    else:

        return 0 <= pt[0] <= 6