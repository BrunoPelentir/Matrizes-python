'''
Matrizes são vetores bidimensionais, ou seja, possuem linhas e colunas.
Geralmente utiizamos a variável com o nome i para nos referirmos
 as linhas e a variável com o nome j para nos referirmos as colunas
'''
import enum


Matriz = [
    [1, 2 , 3, 4] # linha 0
    [8, 7, 11, 13] # linha 1
    [10, 9, 15, 20] # linha 2
    [5, 16, 18, 21] # linha 3
 #   0   1   2   3 coluna
]

matriz = []

#cadastrando os valores na matriz 3x3
for i in range(3): #esse for percorre as linhas da matriz
    linha = [] #a linha que vai ser adicionada na matriz é resetada a cada nova linha

    for j in range(3): #esse for percorre as colunas da matriz
        numero = int(input(f"Digite o valor da matriz na posição [{i}][{j}]: "))
        linha.append(numero)

    matriz.append(linha) # Adicionando a linha preenchida na matriz. Ex: [1, 2, 3]

soma = 0
for i, linha in enumerate(matriz): #enumerate() -> Retorna em qual iteração o laço está e o valor do elemento atual
    for j, valor in enumerate(linha):
        # Para saber os elementos que estão acima do diagonal principal:
        if i < j:
            soma += valor
print(f"Matriz: {matriz}")
print(f"soma: {soma}")