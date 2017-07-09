# Definição recursiva: lista sem elementos repetidos

# Escreva uma definição recursiva para a função norep(xs), cuja avaliação associe uma lista similar a xs porém sem nenhum elemento repetido.

def norep(xs):

    if len(xs) == 0:

        return []

    elif xs[0] not in xs[1:]:

        return [xs[0]] + norep(xs[1:])

    else:

        return norep(xs[1:])