# Definição recursiva: lista sem elementos repetidos

# Escreva uma definição recursiva para a função norep(xs), cuja avaliação associe uma lista similar a xs porém sem nenhum elemento repetido.

def ocorre(k, xs):

    return len([x for x in xs if x == k]) > 0

def norep(xs):

    if len(xs) == 0:

        return []

    elif not ocorre(xs[0], xs[1:]):

        return [xs[0]] + norep(xs[1:])

    else:

        return norep(xs[1:])