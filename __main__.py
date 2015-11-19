import sys

from io import io_operation as ioo
from algorithm import memory_based

def main(argv):
	input_file = ioo.read_file(argv[0])
	matrix = input_file.read_matrix()
	mb = memory_based.memory_based(matrix)
	print mb.predict_rating(11, 608, knn=30)

if __name__ == '__main__':
	main(sys.argv[1:])
