import sys

from inout import read_file
from algorithm import memory_based

def main(argv):
	# Le arquivo de avaliacoes e carrega matriz
	input_file = read_file.read_file(argv[0])
	matrix = input_file.read_matrix()
	
	# Inicia a classe para predicao
	mb = memory_based.memory_based(matrix)
	
	# Calcula nota e imprime em tela
	print("Predicoes")
	print(mb.predict_rating(11, 1094, knn=0, type_alg = "row"))
	print(mb.predict_rating(8, 3155, knn=0, type_alg = "row"))
	print(mb.predict_rating(2793, 3004, knn=0, type_alg = "row"))
	print(mb.predict_rating(2953, 608, knn=0, type_alg = "row"))
	print(mb.predict_rating(3034, 2907, knn=0, type_alg = "row"))

if __name__ == '__main__':
	main(sys.argv[1:])
