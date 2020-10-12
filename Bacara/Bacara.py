# EP - Design de Software
# Equipe: Giancarlo Vanoni Ruggiero
# Data: 09/10/2020

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