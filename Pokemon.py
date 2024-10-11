from random import randint
matriz=[]
n=int(input("Informe o tamanho/a ordem da matriz (precisa ser um número impar): "))
q=int(input("Informe qual o tamanho do quadrado interno a ser analisado (precisa ser menos da metade da ordem da matriz; Ex: Ordem - 7 e Quadrado - 3): "))


if n%2!=0 and q<=n//2:#o código de fato só será executado se o número for ímpar
    for i in range(n):
        linha=[]
        for j in range(n):
            itens_matriz=randint(0, 8)
            linha.append(itens_matriz)
        matriz.append(linha)

    mediana=(n//2)#acho a mediana para encontrar o valor que está no centro da matriz para depois subtituir pelo 9

    matriz[mediana][mediana]=9#aqui insiro o número 9 no centro da matriz, como pedido(pra isso achei a mediana antes)
    
    print("\n############# MATRIZ #############\n")

#aqui imprimo a matriz normal
    for i in range(n):
        for j in range(n):
             print(matriz[i][j], end=" ")
        print()

    print()

    somadorexterno=0
    somadorinterno=0

#######################quadrado principal#####################

#agora vou achar os números que formam o quadrado, até os de dentro dele
    for i in range(mediana-q, mediana+q+1):
        for j in range(mediana-q, mediana+q+1):
            #print(matriz[i][j], end=" ") #se quiser imprimir o quadrado principal, execute essa linha de código e o print inferior
            somadorexterno=somadorexterno+matriz[i][j]#somar todos os números do quadrado como um todo
        #print()
    
    #para verificar a soma dos números como um todo(interno e o das bordas) executar a linha abaixo
    # print(f"a soma de todos os números do quadrado principal é {somadorexterno}") 

#OBS: o pensamento para o range, foi que em uma matriz quadrada de 7, o 9 estaria no [3,3], sendo que 4 é a mediana de 7,...
#...então é o 4 item na 3 posição, já que começa com 0. E o +q seria para selecionar somente os itens/tamanho do quadrado que quero,...
#...ou seja, para delimitar o quadrado de acordo com a distância informada no começo, por exemplo eu queria pegar alguns números...
#...antes da linha e coluna do 9 central e alguns depois da linha e coluna do 9 central, por isso o -q (pegar números antes) e o +q...
#...(para pegar números depois), e o +1 seria pois não é pego o último número nos ranges, mas eu queria pegar, então coloquei +1

########################quadrado interno####################

#agora vou achar só os números que estão dentro do quadrado, sem os números das bordas
    for i in range(mediana-q+1, mediana+q):
        for j in range(mediana-q+1, mediana+q):
            #print(matriz[i][j], end=" ") #se quiser imprimir o quadrado interno, execute essa linha de código e o print inferior
            somadorinterno=somadorinterno+matriz[i][j]#somar todos os números internos, sem as bordas
        #print()

    #para verificar a soma dos números internos executar a linha abaixo
    # print(f"a soma dos números de internos do quadrado é {somadorinterno}") 

##############################resultado################################
    resultado=somadorexterno-somadorinterno #aqui pego a soma de todos os números do quadrado e...
#...tiro a soma dos números que estão no interior do quadrado, me sobrando a soma dos números da borda, que é o que eu quero
    print("############# RESULTADO #############\n")
    print(f"O resultado da soma de todos os números que formam a borda/perímetro do quadrado interno, que demostra as importâncias dos pokemons pegos, é: {resultado}")

else:
    print("Execução da caçada pokemon não viável, pois o número da ordem da matriz precisa ser ímpar e o número do quadrado interno precisa ser menor do que a metade da ordem da matriz")