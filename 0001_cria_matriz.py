import random     #chama o random para não precisar dar entrada nos valores da matriz

n = int(input("números de linhas:"))
m = int(input("números de colunas:"))

matriz=[]
for i in range (n):
    linha=[]
    for j in range(m):
        linha.append(random.randint(1,9))    #especifica a entrada dos números compreendidos no intervalo que vc escolher
    matriz.append(linha)    #append é a função de adicionar, 1° eu escolho o local destino e dps digo o elemento

print(*matriz)    #vou imprimir a matriz
