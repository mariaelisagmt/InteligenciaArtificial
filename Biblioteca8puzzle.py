
class Problema:
	# tipo abstrato de dado problema definido no capitulo 3 do livro de IA ou nos slides
	# da aula 3

	def __init__(self, estado_inicial, operadores, teste_meta, funcao_custo):
		"""
		Construtor de uma classe problema. O construtor recebe como parametros todos
		os componentes de um problema para construir um.
		@param estado_inicial: estado inicial que se encontra o problema
		@param operadores: operadores que executam sobre o problema
		@param teste_meta: funcao que testa para ver se alcancamos o estado desejado
		@param funcao_custo: calcula a distancia do estado atual ao estado meta
		"""
		self.estado_inicial = estado_inicial
		self.operadores = operadores
		self.teste_meta = teste_meta
		self.funcao_custo = funcao_custo
		self.comparacoes = 0

class No:
	# para realizar o algoritmo de busca em arvore, devemos ter o tipo no. O tipo abstrato
	# esta descrito nos slides da aula 3.

	def __init__(self, estado, no_pai, operador, profundidade, custo_caminho):
		"""
		Construtor de um no para busca em arvore.
		@param estado: estado associado ao no corrente
		@param no_pai: no que deu origem ao no atual. "None" caso ele seja raiz
		@param operador: operador associado ao no
		@param profundidade: profundidade que no se encontra
		@param custo_caminho: custo do no atual ate o no raiz
		"""
		self.estado = estado
		self.no_pai = no_pai
		self.operador = operador
		self.profundidade = profundidade
		self.custo_caminho = custo_caminho


def expande(no, problema):
	"""
	Funcao que expande um no e gera um conjunto de filhos
	@param no: no atual a ser expandido
	@param problema: problema no qual o no se encontra
	"""
	filhos = [] # conjunto de filhos gerados por um determinado no

	for operacao in problema.operadores:
		resultado = operacao(no.estado)

		# se o no produz algum filho, entao coloque ele no conjunto de filhos
		if not resultado is None:
			# criando um novo no a partir da expansao do no atual
			filhos.append(No(resultado, operacao, no, no.profundidade + 1, no.custo_caminho + problema.funcao_custo(resultado)))

	# retornando o conjunto resultante da expansao
	return filhos

def expande1(no, problema):
	"""
	Funcao que expande um no e gera um conjunto de filhos. Essa eh a versao alternativa para a busca gulosa.
	@param no: no atual a ser expandido
	@param problema: problema no qual o no se encontra
	"""
	filhos = [] # conjunto de filhos gerados por um determinado no

	for operacao in problema.operadores:
		resultado = operacao(no.estado)

		# se o no produz algum filho, entao coloque ele no conjunto de filhos
		if not resultado is None:
			# criando um novo no a partir da expansao do no atual
			filhos.append(No(resultado, operacao, no, no.profundidade + 1, problema.funcao_custo(resultado)))

	# retornando o conjunto resultante da expansao
	return filhos

def expande2(no, problema):
	"""
	Funcao que expande um no e gera um conjunto de filhos. Essa eh a versao alternativa para a busca A*.
	@param no: no atual a ser expandido
	@param problema: problema no qual o no se encontra
	"""
	filhos = [] # conjunto de filhos gerados por um determinado no

	for operacao in problema.operadores:
		resultado = operacao(no.estado)

		# se o no produz algum filho, entao coloque ele no conjunto de filhos
		if not resultado is None:
			# criando um novo no a partir da expansao do no atual
			filhos.append(No(resultado, operacao, no, no.profundidade + 1,no.profundidade + 1 + problema.funcao_custo(resultado)))

	# retornando o conjunto resultante da expansao
	return filhos



def busca(problema, enfileira):
	c = 0
	"""
	Funcao que realiza um algoritmo de busca. A estrategia de busca depende da
	funcao enfileira passada como argumento. Ex: FIFO representa busca em largura
	LIFO representa busca em profundidade.
	@param problema: problema a ser resolvido
	@param enfileira: funcao de enfileiramento de nos
	"""
	nos = [No(problema.estado_inicial, None, None, 0, 0)] # criando uma fila com o estado inicial
	visitados = []
	while (True):
		if nos == []: return None # retorna fracasso caso a lista seja vazia

		no = nos.pop(0)
		#print(problema.teste_meta(no.estado))
		# verifica se o estado atual e a meta
		c = c + 1
		problema.comparacoes = c
		if problema.teste_meta(no.estado): return no.estado
		# caso nao seja a meta, o no e expandido
		if not no.estado in visitados:
			nos = enfileira(expande(no, problema), nos)
			visitados.append(no.estado)
			#print(visitados)
		print (len(nos))

def tira_melhor(nos):
	aux = nos[0]
	for i in nos:
		if aux.custo_caminho > i.custo_caminho:
			aux = i
	nos.remove(aux)
	return aux



def buscagulosa(problema, enfileira):
	c = 0
	"""
	Funcao que realiza um algoritmo de busca. A estrategia de busca depende da
	funcao enfileira passada como argumento. Ex: FIFO representa busca em largura
	LIFO representa busca em profundidade.
	@param problema: problema a ser resolvido
	@param enfileira: funcao de enfileiramento de nos
	"""
	nos = [No(problema.estado_inicial, None, None, 0, 0)] # criando uma fila com o estado inicial
	visitados = []
	while (True):
		if nos == []: return None # retorna fracasso caso a lista seja vazia

		no = tira_melhor(nos)
		#print no.custo_caminho
		#print(problema.teste_meta(no.estado))
		# verifica se o estado atual e a meta
		c = c + 1
		problema.comparacoes = c
		if problema.teste_meta(no.estado): return no.estado
		# caso nao seja a meta, o no e expandido
		if not no.estado in visitados:
			nos = enfileira(expande1(no, problema), nos)
			visitados.append(no.estado)



def buscaaestrela(problema, enfileira):
	c = 0
	"""
	Funcao que realiza um algoritmo de busca. A estrategia de busca depende da
	funcao enfileira passada como argumento. Ex: FIFO representa busca em largura
	LIFO representa busca em profundidade.
	@param problema: problema a ser resolvido
	@param enfileira: funcao de enfileiramento de nos
	"""
	nos = [No(problema.estado_inicial, None, None, 0, 0)] # criando uma fila com o estado inicial
	visitados = []
	while (True):
		if nos == []: return None # retorna fracasso caso a lista seja vazia

		no = tira_melhor(nos)
		#print no.custo_caminho
		#print(problema.teste_meta(no.estado))
		# verifica se o estado atual e a meta
		c = c + 1
		problema.comparacoes = c
		if problema.teste_meta(no.estado): return no.estado
		# caso nao seja a meta, o no e expandido
		if not no.estado in visitados:
			nos = enfileira(expande2(no, problema), nos)
			visitados.append(no.estado)
			#print(visitados)
		#print len(nos)