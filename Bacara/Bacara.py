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