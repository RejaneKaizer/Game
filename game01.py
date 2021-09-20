# Jogo de teste de velocidade, onde o programa pode sortear números, letras, palavras 
# ou sentenças e os jogadores devem digitar o mais rápido para vencer. 
# O jogo deve ser multiplayer, ou seja, pode jogar mais de um jogador por vez.
# O jogo deve possuir um menu inicial, com opções:
#    1 - Jogar
#    2 - Alterar configurações do jogo (Quantidade de jogadores, Quantidade de letras/números/sentenças sorteadas, …)
#    3 - Sair
# O menu deve se repetir até que o usuário escolha a opção 3 - Sair.

from time import sleep, time
from random import randint
from ModulosGame01 import Nomes1, Nomes2, Jogo, Jogo2

print ("▶️ Bem-vindos, jogadores! Esse jogo se trata de um teste de velocidade, ")  
print ("onde quem digitar mais rápido as sentenças dadas vence! Vocês estão prontos???")
sleep (4)
print ("\n⚠️ E lembrem-se: sejam rápidossss!!! Vamos lá!")
sleep(1)
print("\n🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃")

sleep (3) #Pausa antes de mostrar o Menu do jogo.

Menu = """

##########################
      Menu Principal
##########################

[ 1 ] Jogar (⭐ 2 jogadores e 1 sentença de cada ⭐)

[ 2 ] Alterar configurações do jogo 
( Quantidade de jogadores; Quantidade de letras/números/sentenças ou palavras. )  

[ 3 ] Sair

"""
while True:
    print (f" \033[33m {Menu}") #Edição de cores no terminal do Menu do jogo.
    
    sleep (1)
    
    Opção = float (input ("\033[37m▶️ Digite a opção desejada do Menu acima: "))
    
    if Opção != 1 and Opção != 2 and Opção != 3 :
        print("⚠️ Opção inválida! Você retornará ao Menu.")
        sleep (1)

    elif Opção == 1 :
        
        Jogo()
        sleep (2)
    
    elif Opção == 2 :
        
        AlterarQuant =  input ("\n▶️ Você deseja alterar a quantidade de jogadores ou de sentenças? (Sim ou Não) : ")
        sleep (1)

        if AlterarQuant == "Sim" or AlterarQuant == "sim" :
            Jogo2 ()
            sleep (2)

        elif AlterarQuant == "Não" or AlterarQuant == "não" or AlterarQuant == "Nao" or AlterarQuant == "nao" :
            print ("\n➡️ O jogo terá, então, apenas 2 jogadores e 1 sentença de cada tipo!")
            sleep(2)
            Jogo()

        else :
            print("⚠️ Opção inválida! Você retornará ao Menu.")
            sleep (2)
            
        sleep (1)
    
    else :
        print ("\n❗Você digitou sair do jogo. Obrigado por participar!😄")
        break   











    







