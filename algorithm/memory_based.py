import operator
from math import sqrt

class memory_based:

	matrix = []

	'''
	__init__: Construtor da classe
	Parametros: <matriz> - Matriz de usuarios vs item
	Obs.: A matriz nao exige padrao, ou seja, usuarios podem
		estar nas linhas e itens nas colunas, ou vice e versa.
	'''
	def __init__(self, matrix):
		self.matrix = matrix
	
	'''
	predict_rating: Prediz a avaliação de um par de entidades (usuário -> item)
	Parâmetris: <row> ID da entidade alvo na linhas
				<col> ID da entidade alvo na colunas
				<knn> Numero de vizinhos que sera utilizado
				<type_alg> Tipo do algoritmo ("row" ou "col")
					Exemplo: Dada uma matriz (Usuarios nas linhas e 
						itens nas colunas).
						Se type_alg == "row", sera executado o algoritmos baseado em usuario.
						Se type_alg == "col" sera executado o algoritmo baseado em item
	'''
	def predict_rating(self, row, col, knn = 0, type_alg = "row"):
		hash_sim = dict()
		rating = 0
		numerator = 0
		denominator = 0
		
		# Vetor armazena a similaridade entre vizinhos
		vector_sim = self.calculate_similarity(row, col, type_alg)

		# Apenas k vizinhos sao mantidos para calculo
		if knn < len(vector_sim) and knn > 0:
			vector_sim = vector_sim[(len(vector_sim) - knn):]
		
		# Transfere dados da similaridade para uma tabela hash
		for tuple_sim in vector_sim:
			hash_sim[tuple_sim[0]] = tuple_sim[1]

		# Recupera vetor alvo para o calculo
		if type_alg == "row":
			vector_target = self.matrix[row]
		else:
			vector_target = [line[col] for line in self.matrix]

		# Inicia rating com a media
		rating = float(sum(vector_target))/len(vector_target)
		
		row_size = len(self.matrix[0])
		col_size = len([value[0] for value in self.matrix])
		
		# Percore a tabela hash de similaridades
		for key in hash_sim:
			if type_alg == "row":
				# Calcula a media da linha
				mean_row = sum([value for value in self.matrix[key]]) / row_size
				
				# Calcula o numerador para a media centrada
				numerator += hash_sim[key] * (self.matrix[key][col] - mean_row)
			else:
				# Calcula media da coluna
				mean_col = sum([line[key] for line in self.matrix]) / col_size
				
				# Calcula o numerador para a media centrada
				numerator += hash_sim[key] * (self.matrix[row][key] - mean_col)

			# Calcula o denominador para a media centrada
			denominator += abs(hash_sim[key])

		# Prediz o rating e retorna com 5 casas decimais
		rating += numerator / denominator
		return round(rating,5)

	'''
	calculate_similarity: Calcula a similaridade entre as linhas ou colunas
	Parametros: <row> Linha alvo
				<col> Coluna alvo
				<type_alg> Tipo do algoritmo ("row" ou "col")
					Exemplo: Dada uma matriz (Usuarios nas linhas e 
						itens nas colunas).
						Se type_alg == "row", sera executado o algoritmos baseado em usuario.
						Se type_alg == "col" sera executado o algoritmo baseado em item
	'''
	def calculate_similarity(self, row, col, type_alg):
		hash_sim = dict()
		
		# Verifica qual algoritmos deve ser executado
		if type_alg == "row":
			vector_target = self.matrix[row][:]
			# Salva a similaridade para linha
			for id_row in range(len(self.matrix)):
				if self.matrix[id_row][col] > 0:
					hash_sim[id_row] = self.vector_cosine(vector_target, self.matrix[id_row])
		else:
			vector_target = [line[col] for line in self.matrix]
			# Salva a similaridade para coluna
			for id_col in range(len(self.matrix[0])):
				if self.matrix[row][id_col] > 0:
					hash_sim[id_col] = self.vector_cosine(vector_target, [line[id_col] for line in self.matrix])
		
		# Retorna um VETOR de TUPLAS ordenado pelo valor crescente
		return sorted(hash_sim.items(), key=operator.itemgetter(1))
	
	'''
	square_rooted: Calcula raiz do quadrado para calculo do coseno
	Parametros: <vector> Vetor de valores para calcular a raiz da soma ao quadrado
	'''
	def square_rooted(self, vector):
		return round(sqrt(sum([value**2 for value in vector])),5)

	'''
	vector_cosine: Calcula a similaridade do coseno entre dois vetores
	Parametros: <vector_one> Primeiro vetor
				<vector_tow> Segundo vetor
	'''
	def vector_cosine(self, vector_one, vector_two):
		numerator = sum(value_one * value_two for value_one,value_two in zip(vector_one,vector_two))
		denominator = self.square_rooted(vector_one) * self.square_rooted(vector_two)
		return round(numerator/float(denominator),5)
