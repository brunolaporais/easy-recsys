import sys
class read_file:

	input_file = None

	def __init__(self, rating_file):
		self.input_file = open(rating_file)

	def read_matrix(self, format = {"row":0, "col":1, "value":2}):
		print("Lendo arquivo")

		matrix = []
		hash_auxiliar = dict(dict())
		line = self.input_file.readline()
		line = line.replace('\n','')
		tuple_line = line.split("::")
		max_col = 0
		i = 1

		while len(line) > 1:
			#Status feecback
			print("\r"+str(i)),
			sys.stdout.flush()
			row_key = int(tuple_line[format["row"]])
			col_key = int(tuple_line[format["col"]])
			value = int(tuple_line[format["value"]])
			if not hash_auxiliar.has_key(row_key):
				hash_auxiliar[row_key] = dict()

			hash_auxiliar[row_key][col_key] = value
			
			if max_col < col_key:
				max_col = col_key

			line = self.input_file.readline()
			tuple_line = line.replace('\n','')
			tuple_line = line.split("::")
			i += 1

		matrix = [[0 for i in range(max_col+1)] for j in range(len(hash_auxiliar) + 1)]
		for row in hash_auxiliar:
			for col in hash_auxiliar[row]:
					matrix[row][col] = hash_auxiliar[row][col]
		print("... OK!")

		self.input_file.close()
		hash_auxiliar = None
		return matrix
