# EP - Design de Software
# Equipe: Giancarlo Vanoni Ruggiero
# Data: 09/10/2020

import random

print("Bem-vindo ao jogo bacará")
#Quantidade de fichas do jogador
fichas=100 

#Baralho 1 adicionado
Baralho1=[1,2,3,4,5,6,7,8,9,0,0,0,0]*4 

#Quantidade de fichas a serem apostadas:
aposta=int(input("Diga quantas fichas você deseja apostar, um valor entre 1 e {0}: ".format(fichas)))

#Caso o jogador digite um valor inválido de fichas
while aposta> fichas or aposta<=0: 
    aposta=int(input("Digite um valor válido de fichas entre 1 e {0}: ".format(fichas)))

#Para o jogador decidir quem irá ganhar
ganhador=input("Deseja apostar na banca, no jogador ou no empate? Digite banca, jogador ou empate: ")

#Caso não digite o nome correto
while ganhador != "banca" and ganhador != "jogador" and ganhador != "empate": 
        ganhador = input("Digite jogador, banca ou empate: ")

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
    if jogador > banca and ganhador == "jogador":
        fichas=aposta+fichas
    elif jogador> banca:
        fichas=fichas - aposta
    elif jogador < banca and ganhador == "banca":
        fichas=fichas+int(0.95*aposta)
    elif jogador < banca:
        fichas=fichas - aposta
    elif banca == jogador and ganhador == "empate":
        fichas = fichas + 8*aposta
    elif jogador == banca:
        fichas = fichas - aposta
    return fichas

#Caso a soma das duas cartas da banca e/ou jogador seja 8 ou 9
if soma_banca== 8 or soma_banca==9 or soma_jogador==8 or soma_jogador==9:
    fichas= comparar(soma_jogador,soma_banca, ganhador, aposta, fichas)

