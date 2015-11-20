class read_file:

	input_file = None

	'''
	__init__: Construtor
	Parametros: <rating_file> Arquivo de dados à carregar
	'''
	def __init__(self, rating_file):
		self.input_file = open(rating_file)

	'''
	read_matrix: Carrega do arquivo para matriz
	Parametros: <format> Tabela hash contendo posicao 
				da linha, coluna e valor no arquivo.
	'''
	def read_matrix(self, format = {"row":0, "col":1, "value":2}):
		print("Lendo arquivo")

		matrix = []
		hash_auxiliar = dict(dict())
		line = self.input_file.readline()
		line = line.replace('\n','')
		tuple_line = line.split("::")
		max_col = 0
		i = 1

		# Le arquivo ate o final
		while len(line) > 1:
			# Feedback de status
			if i % 100000 == 0:
				print(str(i) + "... Linhas Processadas")
				
			# Adiciona o par (usuario e item) na tabela hash
			row_key = int(tuple_line[format["row"]])
			col_key = int(tuple_line[format["col"]])
			value = int(tuple_line[format["value"]])
			if row_key not in hash_auxiliar:
				hash_auxiliar[row_key] = dict()
			hash_auxiliar[row_key][col_key] = value
			
			# Armazena quantidade de colunas para gerar a matriz
			if max_col < col_key:
				max_col = col_key

			line = self.input_file.readline()
			tuple_line = line.replace('\n','')
			tuple_line = line.split("::")
			i += 1

		print("Carregando matriz"),
		matrix = [[0 for i in range(max_col+1)] for j in range(len(hash_auxiliar) + 1)]
		for row in hash_auxiliar:
			for col in hash_auxiliar[row]:
					matrix[row][col] = hash_auxiliar[row][col]
		print("... OK!")

		self.input_file.close()
		hash_auxiliar = None
		return matrix