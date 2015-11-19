import operator
from math import sqrt

class memory_based:

	matrix = []

	def __init__(self, matrix):
		self.matrix = matrix
	
	'''
	type_alg = row:row_based, col:col_based
	'''
	def predict_rating(self, row, col, knn = 0, type_alg = "row"):
		hash_sim = dict()
		rating = 0
		vector_sim = self.calculate_similarity(row, col, type_alg)

		if knn < len(vector_sim):
			for id_pos in range(len(vector_sim)):
				if knn > 0:
					del vector_sim[id_pos]
					knn -= 1

		for tuple_sim in vector_sim:
			hash_sim[tuple_sim[0]] = tuple_sim[1]

		if type_alg == "row":
			vector_target = self.matrix[row]
		else:
			vector_target = [line[col] for line in self.matrix]

		rating = float(sum(vector_target))/len(vector_target)

		numerator = 0
		denominator = 0
		row_size = len(self.matrix[0])
		col_size = len([value[0] for value in self.matrix])
		for key in hash_sim:			
			if type_alg == "row":
				mean_row = sum([value for value in self.matrix[key]]) / row_size
				numerator += hash_sim[key] * (self.matrix[key][col] - mean_row)
			else:
				mean_col = sum([line[key] for line in self.matrix]) / col_size
				numerator += hash_sim[key] * (self.matrix[row][key] - mean_col)

			denominator += abs(hash_sim[key])

		rating += numerator / denominator
		return rating

	def calculate_similarity(self, row, col, type_alg):
		hash_sim = dict()
		if type_alg == "row":
			vector_target = self.matrix[row][:]
			for id_row in range(len(self.matrix)):
				if self.matrix[id_row][col] > 0:
					hash_sim[id_row] = self.vector_cosine(vector_target, self.matrix[id_row])
		else:
			vector_target = [line[col] for line in self.matrix]
			for id_col in range(len(self.matrix[0])):
				if self.matrix[row][id_col] > 0:
					hash_sim[id_col] = self.vector_cosine(vector_target, [line[id_col] for line in self.matrix])
		return sorted(hash_sim.items(), key=operator.itemgetter(1))
	
	def square_rooted(self, vector):
		return round(sqrt(sum([value**2 for value in vector])),5)

	def vector_cosine(self, vector_one, vector_two):
		numerator = sum(value_one * value_two for value_one,value_two in zip(vector_one,vector_two))
		denominator = self.square_rooted(vector_one) * self.square_rooted(vector_two)
		return round(numerator/float(denominator),5)
