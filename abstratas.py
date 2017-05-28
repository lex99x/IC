# Retorna soma de a e b, complementa as funções com reduce

def soma(a, b):

    return a + b

# Retorna lista de elementos maiores que x em l, complementa a função maior

def maiores_que(x, l):

    return [y for y in l if y > x]

# Retorna o maior elemento em l (int)

def maior(l):

    return [x for x in l if maiores_que(x, l) == []][0]

# Verifica se n é múltiplo de cinco (boolean)

def multiplo_de_cinco(n):

    return n % 5 == 0