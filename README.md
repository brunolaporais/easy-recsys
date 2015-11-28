# easy-recsys

Implementação dos métodos clássicos em Sistemas de Recomendação.

## Exemplo:

# Lendo arquivo de avaliações e carrega matriz
input_file = read_file.read_file(argv[0]) # Arquivo de avaliações
matrix = input_file.read_matrix(format = {"row":0, "col":1, "value":2}) # Formato do arquivo de entrada

# Inicia a classe com métodos baseado em memória
mb = memory_based.memory_based(matrix)

# Calcula nota e imprime em tela
print(mb.predict_rating(11, 1094, knn=0, type_alg = "row"))
print(mb.predict_rating(8, 3155, knn=0, type_alg = "col"))
