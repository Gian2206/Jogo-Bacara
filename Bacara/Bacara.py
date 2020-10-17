# EP - Design de Software
# Equipe: Giancarlo Vanoni Ruggiero
# Data: 09/10/2020

#Importa biblioteca random
import random

print("Bem-vindo ao jogo bacará")

#Pergunta o número de jogadores
numero_de_jogadores = int(input("Digite o número de jogadores: "))

#Caso não digite um número de jogadores válido
while numero_de_jogadores<1:
    numero_de_jogadores =int(input("Digite um valor acima de 1 para definir a quantidade de jogadores: "))

lista_jogadores=[]
lista_apostas=[]
lista_tipo_de_aposta=[] 
n=1
j=0

#Cria lista com jogadores
while numero_de_jogadores>len(lista_jogadores):
    jogador = "jogador "+ str(n)
    lista_jogadores.append(jogador)
    n+=1
    
#Quantidade de fichas do jogador
fichas=100 

#Cria lista com o número de fichas de cada jogador
lista_fichas=[fichas]*numero_de_jogadores

#Mais baralhos adicionados
n= int(input("Deseja jogar com 1, 6, ou 8 baralhos? "))

#Caso seja um valor de baralhos diferente de 1, 6 ou 8
while n!= 1 and n!= 6 and n!=8:
    n= int(input("Digite 1, 6 ou 8 para definir o número de baralho "))

#Baralho 1 adicionado
Baralho1=[1,2,3,4,5,6,7,8,9,0,0,0,0]*4*n
while j<len(lista_jogadores):
    #Quantidade de fichas a serem apostadas:
    aposta=int(input("{0}, diga quantas fichas você deseja apostar, um valor entre 1 e {1}: ".format(lista_jogadores[j], lista_fichas[j])))

    #Caso o jogador digite um valor inválido de fichas
    while aposta> fichas or aposta<=0: 
        aposta=int(input("Digite um valor válido de fichas entre 1 e {0}: ".format(lista_fichas[j])))
    
    lista_apostas.append(aposta)

    #Para o jogador decidir quem irá ganhar
    ganhador=input("{0}, deseja apostar na banca, no jogador ou no empate? Digite banca, jogador ou empate: ".format(lista_jogadores[j]))

    #Caso não digite o nome correto
    while ganhador != "banca" and ganhador != "jogador" and ganhador != "empate": 
        ganhador = input("Digite jogador, banca ou empate: ")

    lista_tipo_de_aposta.append(ganhador)
    j+=1

j=0

#Sorteia primeira carta do jogador
sorteio_jogador1 = random.choice(Baralho1)

#Tira a "carta" do baralho (no caso retira da lista o valor da carta) 
del Baralho1[Baralho1.index(sorteio_jogador1)]

#Realiza o sorteio da segunda carta do jogador
sorteio_jogador2 = random.choice(Baralho1)

#Tira a "carta" do baralho (no caso retira da lista o valor da carta) 
del Baralho1[Baralho1.index(sorteio_jogador2)]

#Soma as cartas do jogador
soma_jogador = sorteio_jogador1+sorteio_jogador2

#Transforma em string a variável soma_jogador
soma_jogador = str(soma_jogador)

#A variável soma_jogador recebe o valor das unidades 
soma_jogador = int(soma_jogador[len(soma_jogador)-1])

#Sorteia primeira carta da banca
sorteio_banca1 = random.choice(Baralho1)

#Tira a "carta" do baralho (no caso retira da lista o valor da carta) 
del Baralho1[Baralho1.index(sorteio_banca1)]

#Realiza o sorteio da segunda carta da banca 
sorteio_banca2 = random.choice(Baralho1) 

#Tira a "carta" do baralho (no caso retira da lista o valor da carta) 
del Baralho1[Baralho1.index(sorteio_banca2)]

#Soma as cartas da banca
soma_banca = sorteio_banca1+sorteio_banca2

#Transforma em string a variável soma_banca
soma_banca = str(soma_banca)

#A variável soma_banca recebe o valor das unidades 
soma_banca = int(soma_banca[len(soma_banca)-1])

#Função para decidir o ganhador
def comparar(jogador, banca, ganhador,aposta, fichas):
        #Se o jogador apostar nele mesmo e o jogador ganhar
    if jogador > banca and ganhador == "jogador":
        fichas=aposta+fichas
    #Se o jogador ganhar e não tiver apostado nele mesmo    
    elif jogador> banca:
        fichas=fichas - aposta
    #Se a banca ganhar e o jogador tiver apostado na banca
    elif jogador < banca and ganhador == "banca":
        fichas=fichas+int(0.95*aposta)
    #Se a banca ganhar e o jogador não tiver apostado na banca
    elif jogador < banca:
        fichas=fichas - aposta
    #Se der empate e o jogador tiver apostado no empate        
    elif banca == jogador and ganhador == "empate":
        fichas = fichas + 8*aposta
    #Se der empate e o jogador não tiver apostado no empate
    elif jogador == banca:
        fichas = fichas - aposta
    return fichas

#Caso a soma das duas cartas da banca e/ou jogador seja 8 ou 9
if soma_banca== 8 or soma_banca==9 or soma_jogador==8 or soma_jogador==9:
    while j<len(lista_jogadores):
    #Chama a função para decidir o ganhador 
        fichas= comparar(soma_jogador,soma_banca, lista_tipo_de_aposta[j], lista_apostas[j], lista_fichas[j])
        lista_fichas[j]=fichas
        print("{0}, você possui {1} fichas no total".format(lista_jogadores[j],lista_fichas[j]))
        j+=1 
    j=0
#Caso a soma do jogador ou da banca seja menor ou igual a 5
elif soma_banca <= 5 or soma_jogador <= 5:
    #Caso a soma do jogador seja menor ou igual a 5
    if soma_jogador <= 5:
        #Sorteia a terceira carta do jogador
        sorteio_jogador3 = random.choice(Baralho1)

        #Tira a "carta" do baralho (no caso retira da lista o valor da carta) 
        del Baralho1[Baralho1.index(sorteio_jogador3)]
        
        #Soma as cartas do jogador
        soma_jogador = soma_jogador+sorteio_jogador3

        #Transforma em string a variável soma_jogador
        soma_jogador = str(soma_jogador)

        #A variável soma_jogador recebe o valor das unidades 
        soma_jogador = int(soma_jogador[len(soma_jogador)-1])    
    
    #Caso a soma da banca seja menor ou igual a 5
    if soma_banca <= 5:
        
        #Sorteia a terceira carta da banca
        sorteio_banca3 = random.choice(Baralho1)

        #Tira a "carta" do baralho (no caso retira da lista o valor da carta) 
        del Baralho1[Baralho1.index(sorteio_banca3)]
        
        #Soma as cartas do jogador
        soma_banca = soma_banca+sorteio_banca3

        #Transforma em string a variável soma_jogador
        soma_banca = str(soma_banca)

        #A variável soma_jogador recebe o valor das unidades 
        soma_banca = int(soma_banca[len(soma_banca)-1])    
    
    while j<len(lista_jogadores):
    #Chama a função para decidir o ganhador 
        fichas= comparar(soma_jogador,soma_banca, lista_tipo_de_aposta[j], lista_apostas[j], lista_fichas[j])
        lista_fichas[j]=fichas
        print("{0}, você possui {1} fichas no total".format(lista_jogadores[j],lista_fichas[j]))
        j+=1 
else:
    while j<len(lista_jogadores):
    #Chama a função para decidir o ganhador 
        fichas= comparar(soma_jogador,soma_banca, lista_tipo_de_aposta[j], lista_apostas[j], lista_fichas[j])
        lista_fichas[j]=fichas
        print("{0}, você possui {1} fichas no total".format(lista_jogadores[j],lista_fichas[j]))
        j+=1   
