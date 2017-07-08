# (1) Análise do problema e plano de solução (texto descritivo) – inclusive justificativa das estratégias utilizadas:

# Entendido o problema, o próximo passo é se perguntar se algo semelhante já foi feito: resolução de problemas usando recursão foi uma atividade frequente ao final da disciplina, porém até então não havíamos abordados problemas que envolvessem índices de lista no paradigma recursivo. Sendo assim, minha estratégia foi criar uma outra função que além dos dois parâmetros da função onde, recebe um parâmetro i que servirá de incrementador toda vez que a função for executada. Nessa função, sempre que a condição do problema ocorrer (um valor da lista for igual ao procurado), tudo que precisamos fazer é concatenar o valor corrente de i em uma lista (que é retornada ao final da recursão) e seguir em frente, caso contrário, simplesmente ignoramos o valor verificado e da mesma forma seguimos em frente com a recursão até que a lista esteja vazia.

# (2) Solução em Python:

def find_indexes(x, xs, i):

	if len(xs) == 0:

		return []

	elif xs[0] == x:

		return [i] + find_indexes(x, xs[1:], i + 1)

	else:

		return find_indexes(x, xs[1:], i + 1)

def onde(x, xs):

	return find_indexes(x, xs, 0)

# (3) Rastreamento da solução (esquema descritivo “passo-a-passo”, não apenas o resultado) utilizando as 12 primeiras letras de seu nome e a vogal 'o':

# >>> onde('o', 'alex andre r'): len('alex andre r') == 0 => False, 'a' == 'o' => False 
	
# 	>>> onde('o', 'lex andre r'): len('lex andre r') == 0 => False, 'l' == 'o' => False 
	
# 		>>> onde('o', 'ex andre r'): len('ex andre r') == 0 => False, 'e' == 'o' => False

# 			>>> onde('o', 'x andre r'): len('x andre r') == 0 => False, 'x' == 'o' => False

# 				>>> onde('o', ' andre r'): len(' andre r') == 0 => False, ' ' == 'o' => False

# 					>>> onde('o', 'andre r'): len('andre r') == 0 => False, 'a' == 'o' => False

# 						>>> onde('o', 'ndre r'): len('ndre r') == 0 => False, 'n' == 'o' => False

# 							>>> onde('o', 'dre r'): len('dre r') == 0 => False, 'd' == 'o' => False

# 								>>> onde('o', 're r'): len('re r') == 0 => False, 'r' == 'o' => False

# 									>>> onde('o', 'e r'): len('e r') == 0 => False, 'e' == 'o' => False

# 										>>> onde('o', ' r'): len(' r') == 0 => False, ' ' == 'o' => False

# 											>>> onde('r'): len('r') == 0 => False, 'r' == 'o' => False 

# 												>>> onde('o', ''): len('') == 0 => True | Retorno: []