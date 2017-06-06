import random     #chama o random para não precisar dar entrada nos valores da matriz

n = int(input("números de linhas:")) 
m = int(input("números de colunas:"))

matriz=[]
for i in range (n):
    linha=[]
    for j in range(m):
        linha.append(random.randint(1,9))    # funçao "random.randint(x,y)" especifica a entrada dos números compreendidos no intervalo que vc escolher
    matriz.append(linha)    #append é a função de adicionar, 1° eu escolho o local destino e dps digo o elemento


#vou imprimir a matriz

c=0 #o contador é 0 pq nas posições não se começa do 1.
while c < (len(matriz)):#minha condição é c < numero de termos(q no caso são linhas) na lista "matriz"
    print(*matriz[c]) # o "*" é usado para tirar o conchete na impressão
    c = c +1
