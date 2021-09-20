#Aqui se encontram as funções utilizadas no game01.
#Elas serão chamadas à medida que forem necessárias no arquivo do jogo em si.

from time import sleep, time
from random import randint

#Primeiro, fazer a configuração do jogo com apenas 2 jogadores.    

def Nomes1 () :
    Nome1 = input("\nAntes de começarmos, digite o nome do Jogador 1: ") 
    return Nome1


def Nomes2 () :   
    Nome2 = input("Agora, o nome do jogador 2: ")
    return Nome2
    
    
def Jogo () :
    
    Nome1 = Nomes1 ()
    Nome2 = Nomes2 ()

    #Começar o jogo com os números.
    
    Números = ("597" , "649" , "902" , "837") 
    Embaralhar = randint(0,3)
    
    sleep (2)
    print("\n\033[33m❗O jogo já vai começar !", f"\n{Nome1} irá primeiro!")
    sleep(3)

    print ("\n\033[36m         3 ") #Contagem regressiva para o jogo.
    sleep (1)  
    
    print ("\n\033[36m         2 ")
    sleep (1)

    print ("\n\033[36m         1 ")
    sleep (1)

    print ("\n\033[36m  Valendo!!! 🏃🏃🏃🏃🏃") 
    sleep (1)
    
    print("\n\033[37m▶️ Digite o número abaixo e dê enter no final: ")
    sleep(2)

    print("\033[33mO número será --> {} ".format(Números[Embaralhar]))
    sleep(3)
        
    t1 = time () #Começar a marcar o tempo de digitação do Player 1.
    
    Player1= input("\n\033[37m▶️ DIGITEEE: ")
    if Player1 != "597" and Player1 != "649" and Player1 != "902" and Player1 != "837" :
        
        t1 = time ()
        Player1= input("\n⚠️ Número incorreto! Digite novamente: ")
       
        while Player1 != "597" and Player1 != "649" and Player1 != "902" and Player1 != "837" : 
            t1 = time ()
            Player1= input("\n⚠️ Número incorreto! Digite novamente: ")
            
    t2 = time ()
    Numeros1 = t2 - t1
    
    sleep (1)
    print (f"▶ {Nome1} digitou em {Numeros1:3.3} segundos! ")

    sleep (3)
    
    Números = ("597" , "649" , "902" , "837") # Colocar novamente a lista de números e o embaralhador (com nome diferente),
    Embaralhador = randint(0,3)                 # para não aparecer sempre o mesmo item para cada jogador.
    
    print(f"\n▶️ Agora é a vez de {Nome2}:")
    sleep (4)
    
    print("▶️ Digite o número abaixo e dê enter no final: ")
    sleep(2)

    print("\033[33mO número será --> {} ".format(Números[Embaralhador]))
    sleep(3)
       
    t3 = time () #Começar a marcar o tempo de digitação do Player 2.
    
    Player2= input("\n\033[37m▶️ DIGITEEE: ")

    if Player2 != "597" and Player2 != "649" and Player2 != "902" and Player2 != "837" : 
        
        t3 = time () #Resetar novamente o tempo, caso a pessoa digite errado.
        Player2= input("\n⚠️ Número incorreto! Digite novamente: ")
       
        while Player2 != "597" and Player2 != "649" and Player2 != "902" and Player2 != "837" : 
            t3 = time()
            Player2= input("\n⚠️ Número incorreto! Digite novamente: ")
    
    t4 = time ()
    Numeros2 = t4 - t3
    
    sleep (1)
    print (f"▶ {Nome2} digitou em {Numeros2:3.3} segundos! ")

    if Numeros2 > Numeros1 :
        sleep (2)
        print ("\n\033[33mPlacar atual: ", f"\n1º 🥇 | {Nome1}" , f"\n2º 🥈 | {Nome2}")
    
    elif Numeros2 < Numeros1 :
        sleep(2)
        print ("\n\033[33mPlacar atual: ", f"\n1º 🥇 | {Nome2}" , f"\n2º 🥈 | {Nome1}") 

    else :
        sleep (2)
        print ("\n\033[33mPlacar atual: ", f"\n1º 🥇 | {Nome1}" , f"\n1º 🥇 | {Nome2}" , "\nEMPATADOS!")

    #Continuar o jogo com as letras.

    sleep (4)
    Letras = ("A" , "C" , "J" , "Z" ) 
    Embaralhar = randint(0,3)

    print (f"\n\033[37m▶️ Agora, {Nome1}, digite a letra abaixo e dê enter no final:")
    sleep(2)

    print("\033[33mA letra será --> {} ".format(Letras[Embaralhar]))
    sleep(3)
        
    t1 = time () #Começar a marcar o tempo de digitação do Player 1.
    
    Player1= input("\n\033[37m▶️ DIGITEEE: ")
    if Player1 != "A" and Player1 != "C" and Player1 != "J" and Player1 != "Z" : 
    
        t1 = time ()
        Player1= input("\n⚠️ Letra incorreta! Digite novamente: ")
       
        while Player1 != "A" and Player1 != "C" and Player1 != "J" and Player1 != "Z" : 
            t1 = time ()
            Player1= input("\n⚠️ Letra incorreta! Digite novamente: ")

    t2 = time ()
    Letras1 = t2 - t1
    
    sleep (1)
    print (f"▶ {Nome1} digitou em {Letras1:3.3} segundos! ")

    sleep (2)

    Letras = ("A" , "C" , "J" , "Z" ) 
    Embaralhador = randint(0,3)
    
    print(f"\n▶️ Agora é a vez de {Nome2}:")
    sleep (4)
    
    print("▶️ Digite a letra abaixo e dê enter no final: ")
    sleep(2)

    print("\033[33mA letra será --> {} ".format(Letras[Embaralhador]))
    sleep(2)
       
    t3 = time () #Começar a marcar o tempo de digitação do Player 2.
    
    Player2= input("\n\033[37m▶️ DIGITEEE: ") 

    if Player2 != "A" and Player2 != "C" and Player2 != "J" and Player2 != "Z" : 
       
        t3 = time ()
        Player2= input("\n⚠️ Letra incorreta! Digite novamente: ")
       
        while Player2 != "A" and Player2 != "C" and Player2 != "J" and Player2 != "Z" : 
            t3 = time()
            Player2= input("\n⚠️ Letra incorreta! Digite novamente: ")
            
    t4 = time ()
    Letras2 = t4 - t3
    
    sleep (1)
    print (f"▶ {Nome2} digitou em {Letras2:3.3} segundos! ")
        
    sleep (3)
    
    if Letras2 > Letras1 :
        print ("\n\033[33mPlacar atual: ", f"\n1º 🥇 | {Nome1}" , f"\n2º 🥈 | {Nome2}")

    elif Letras2 < Letras1 :
        print ("\n\033[33mPlacar atual: ", f"\n1º 🥇 | {Nome2}" , f"\n2º 🥈 | {Nome1}")

    else :
        print ("\n\033[33mPlacar atual: ", f"\n1º 🥇 | {Nome1}" , f"\n1º 🥇 | {Nome2}" , "\nEMPATADOS!")

    #Jogar com as palavras.

    sleep (4)

    Palavras = ("barco" , "porta" , "corpo" , "grupo" ) 
    Embaralhar = randint(0,3)

    print (f"\n\033[37m▶️ Agora, {Nome1}, digite a palavra abaixo e dê enter no final:")
    sleep(2)

    print("\033[33mA palavra será --> {} ".format(Palavras[Embaralhar]))
    sleep(4)
        
    t1 = time () #Começar a marcar o tempo de digitação do Player 1.
    
    Player1= input("\n\033[37m▶️ DIGITEEE: ")
    if Player1 != "barco" and Player1 != "porta" and Player1 != "corpo" and Player1 != "grupo" : 
        t1 = time()
        Player1= input("\n⚠️ Palavra incorreta! Digite novamente: ")
       
        while Player1 != "barco" and Player1 != "porta" and Player1 != "corpo" and Player1 != "grupo" : 
            t1 = time ()
            Player1= input("\n⚠️ Palavra incorreta! Digite novamente: ")
            
    t2 = time ()
    Palavras1 = t2 - t1
    
    sleep (1)
    print (f"▶ {Nome1} digitou em {Palavras1:3.3} segundos! ") 
    
    sleep (4)
    
    Palavras = ("barco" , "porta" , "corpo" , "grupo" ) 
    Embaralhador = randint(0,3)
    
    print(f"\n▶️ Agora é a vez de {Nome2}:")
    sleep (2)
    
    print("▶️ Digite a palavra abaixo e dê enter no final: ")
    sleep(2)

    print("\033[33mA palavra será --> {} ".format(Palavras[Embaralhador]))
    sleep(4)
       
    t3 = time () #Começar a marcar o tempo de digitação do Player 2.
    
    Player2= input("\n\033[37m▶️ DIGITEEE: ")

    if Player2 != "barco" and Player2 != "porta" and Player2 != "corpo" and Player2 != "grupo" : 
        t3 = time ()
        Player2= input("\n⚠️ Palavra incorreta! Digite novamente: ")
       
        while Player2 != "barco" and Player2 != "porta" and Player2 != "corpo" and Player2 != "grupo" :
            sleep (1)
            t3 = time ()
            Player2= input("\n⚠️ Palavra incorreta! Digite novamente: ")
              
    t4 = time ()
    Palavras2 = t4 - t3
    
    sleep (1)
    print (f"▶ {Nome2} digitou em {Palavras2:3.3} segundos! ")

    sleep (3)

    if Palavras2 > Palavras1 :
        print ("\n\033[33mPlacar atual: ", f"\n1º 🥇 | {Nome1}" , f"\n2º 🥈 | {Nome2}")

    elif Palavras2 < Palavras1 :
        print ("\n\033[33mPlacar atual: ", f"\n1º 🥇 | {Nome2}" , f"\n2º 🥈 | {Nome1}")

    else :
        print ("\n\033[33mPlacar atual: ", f"\n1º 🥇 | {Nome1}" , f"\n1º 🥇 | {Nome2}" , "\nEMPATADOS!")

    #Por fim, jogar com as sentenças.

    sleep (4)

    Sentenças = ("O rato roeu a roupa do rei de Roma." , "Rosas são vermelhas, borboletas são azuis." , "Tudo vale a pena se a alma não é pequena.", "Ontem eu recebi um telegrama.")
    Embaralhar = randint (0,3)
    
    print (f"\n\033[37m▶️ Agora, {Nome1}, digite a sentença abaixo e dê enter no final:")
    sleep(2)

    print("\n\033[33mA sentença será --> {} ".format(Sentenças[Embaralhar]))
    sleep (2) 
    print ("\033[37m❗❗❗Lembre-se : frases começam com letra MAIÚSCULA e terminam com PONTO FINAL.")
    sleep(5)
        
    t1 = time () #Começar a marcar o tempo de digitação do Player 1.
    
    Player1= input("\n▶️ DIGITEEE: ")
    if Player1 != "O rato roeu a roupa do rei de Roma." and Player1 != "Rosas são vermelhas, borboletas são azuis." and Player1 != "Tudo vale a pena se a alma não é pequena." and Player1 != "Ontem eu recebi um telegrama." : 
        sleep (1)
        t1 = time ()
        Player1= input("\n⚠️ Sentença incorreta! Digite novamente: ")
       
        while Player1 != "O rato roeu a roupa do rei de Roma." and Player1 != "Rosas são vermelhas, borboletas são azuis." and Player1 != "Tudo vale a pena se a alma não é pequena." and Player1 != "Ontem eu recebi um telegrama." :  
            t1 = time ()
            Player1= input("\n⚠️ Sentença incorreta! Digite novamente: ")
 
    t2 = time ()
    Sentenças1 = t2 - t1
    
    sleep (1)
    print (f"▶ {Nome1} digitou em {Sentenças1:3.3} segundos! ")

    sleep (4)
    
    Sentenças = ("O rato roeu a roupa do rei de Roma." , "Rosas são vermelhas, borboletas são azuis." , "Tudo vale a pena se a alma não é pequena.", "Ontem eu recebi um telegrama.")
    Embaralhador = randint (0,3)
    
    print(f"\n▶️ Agora é a vez de {Nome2}:")
    sleep (2)
    
    print("\n\033[33mA sentença será --> {} ".format(Sentenças[Embaralhador]))
    sleep (2)
    print ("\033[37m❗❗❗Lembre-se : frases começam com letra MAIÚSCULA e terminam com PONTO FINAL.")
    sleep(5)
       
    t3 = time () #Começar a marcar o tempo de digitação do Player 2.
    
    Player2= input("\n▶️ DIGITEEE: ")

    if Player2 != "O rato roeu a roupa do rei de Roma." and Player2 != "Rosas são vermelhas, borboletas são azuis." and Player2 != "Tudo vale a pena se a alma não é pequena." and Player2 != "Ontem eu recebi um telegrama." :  
        
        t3 = time ()
        Player2= input("\n⚠️ Sentença incorreta! Digite novamente: ")
       
        while Player2 != "O rato roeu a roupa do rei de Roma." and Player2 != "Rosas são vermelhas, borboletas são azuis." and Player2 != "Tudo vale a pena se a alma não é pequena." and Player2 != "Ontem eu recebi um telegrama." :
            t3 = time ()
            Player2= input("\n⚠️ Sentença incorreta! Digite novamente: ")

    t4 = time ()
    Sentenças2 = t4 - t3
    
    sleep (1)
    print (f"▶ {Nome2} digitou em {Sentenças2:3.3} segundos! ")

    sleep (3)

    if Sentenças2 < Sentenças1 :
        print ("\n\033[33mPlacar atual: ", f"\n1º 🥇 | {Nome2}" , f"\n2º 🥈 | {Nome1}")

    elif Sentenças2  > Sentenças1 :
        print ("\n\033[33mPlacar atual: ", f"\n1º 🥇 | {Nome1}" , f"\n2º 🥈 | {Nome2}")

    else :
        print ("\n\033[33mPlacar atual: ", f"\n1º 🥇 | {Nome1}" , f"\n1º 🥇 | {Nome2}" , "\nEMPATADOS!")

    sleep (2)
    print ("\n\033[37mFIM DE JOGO:", f"\033[33m O placar final é: ")
    sleep (2)
    
    #Criar o placar final com base na média de tempos de cada jogador.
    Media1 = (Numeros1 + Letras1 + Palavras1 + Sentenças1) / 4
    Media2 = (Numeros2 + Letras2 + Palavras2 + Sentenças2) / 4


    if Media2 < Media1 :
        print (f"\n\033[37m | 1º 🥇 | {Nome2} |" , f"\n | 2º 🥈 | {Nome1} |")

    elif Media2 > Media1 :
        print (f"\n\033[37m | 1º 🥇 | {Nome1} |" , f"\n | 2º 🥈 | {Nome2} |")

    else :
        print (f"\n\033[37m | 1º 🥇 | {Nome1} |" , f"\n | 1º 🥇 | {Nome2} |" , "\nEMPATADOS!")

    print ("\n\033[33mPARABÉNS AO VENCEDOR!")
    print ("👏🎊👏🎊👏🎊👏🎊👏🎊")
    sleep (2)
    print ("\n\033[37mRetornaremos ao Menu principal.")
    sleep (2)


#Agora, fazer a configuração do jogo com 2 ou mais jogadores.

def Jogo2 () :
    
    Jogador = float (input("➡️ Quantos jogadores serão? Digite um número inteiro (a partir de 1): "))
    Sentença = float (input("➡️ Quantas sentenças de cada tipo serão? Digite um número inteiro (de 1 a 4): "))
            
    sleep (2)
    
    if Jogador < 1 or (Jogador % 1) != 0 or 1 > Sentença > 4 or (Sentença % 1) != 0 : #Testar se os valores são inteiros e válidos.

        print ("\n❗Valores inválidos! Você retornará ao Menu principal do Jogo.")
        sleep (1)
        
    else:
        
        Nomes = []
        TempoIndividual = [] #Lista criada, para armazenar uma média dos tempos de cada jogador e ver qual ganhou.
        TempoTotal = []
        
        i = 0
        while i < Jogador :
            NomesJogadores = input (f"\n➡️ Digite o nome do {i+1}º jogador: ")
            Nomes.append(NomesJogadores)
            
            #Jogador 1 = Nomes [0] ;
            #Jogador 2 = Nomes [1] ...
            #Informação para saber o nome de cada Jogador, com base na posição da lista 'Nomes'.
            
            sleep (1)
            print("\n\033[33m❗O jogo já vai começar !", f"\nE é a vez de {NomesJogadores} jogar.")
            sleep (2)
            print ("\n\033[36m         3 ") #Contagem regressiva para o jogo.
            sleep (1)  
    
            print ("\n\033[36m         2 ")
            sleep (1)

            print ("\n\033[36m         1 ")
            sleep (1)

            print ("\n\033[36m  Valendo!!! 🏃🏃🏃🏃🏃") 
            sleep (1)

            j = 0
            while j < Sentença :
            
            #Começar o jogo com os números.
                sleep (2)
                print (f"\n\033[33m {j+1}º RODADA❗❗❗")

                Números = ("597" , "649" , "902" , "837") 
                Embaralhar = randint(0,3)
    
                print("\n\033[37m▶️ Digite o número abaixo e dê enter no final: ")
                sleep(2)

                print("\033[33mO número será --> {} ".format(Números[Embaralhar]))
                sleep(3)
        
                t1 = time () #Começar a marcar o tempo de digitação do Player.
    
                Player= input("\n\033[37m▶️ DIGITEEE: ")
                
                if Player != "597" and Player != "649" and Player != "902" and Player != "837" :
                    t1 = time()
                    Player= input("\n⚠️ Número incorreto! Digite novamente : ")
       
                    while Player != "597" and Player != "649" and Player != "902" and Player != "837" : 
                        t1 = time ()
                        Player= input("\n⚠️ Número incorreto! Digite novamente : ")

                t2 = time ()
                TempoNumeros = t2 - t1
    
                sleep (1)
                print (f"▶ {NomesJogadores} digitou em {TempoNumeros:3.3} segundos! ")

                sleep (3)

                #Continuar o jogo com as letras.

                Letras = ("A" , "C" , "J" , "Z" ) 
                Embaralhar = randint(0,3)

                print (f"\n▶️ Agora, digite a letra abaixo e dê enter no final:")
                sleep(2)

                print("\033[33mA letra será --> {} ".format(Letras[Embaralhar]))
                sleep(3)
        
                t1 = time () #Começar a marcar o tempo de digitação do Player.
    
                Player= input("\n\033[37m▶️ DIGITEEE: ")
                if Player != "A" and Player != "C" and Player != "J" and Player != "Z" : 
                    
                    t1 = time ()
                    Player= input("\n⚠️ Letra incorreta! Digite novamente: ")
       
                    while Player != "A" and Player != "C" and Player != "J" and Player != "Z" : 
                        t1 = time ()
                        Player= input("\n⚠️ Letra incorreta! Digite novamente: ")
                                
                t2 = time ()
                TempoLetras = t2 - t1
    
                sleep (1)
                print (f"▶ {NomesJogadores} digitou em {TempoLetras:3.3} segundos! ")

                sleep (3)

                #Jogar com as palavras.

                Palavras = ("barco" , "porta" , "corpo" , "grupo" ) 
                Embaralhar = randint(0,3)

                print ("\n▶️ Agora, digite a palavra abaixo e dê enter no final:")
                sleep(2)

                print("\033[33mA palavra será --> {} ".format(Palavras[Embaralhar]))
                sleep(3)
        
                t1 = time () #Começar a marcar o tempo de digitação do Player.
    
                Player= input("\n\033[37m▶️ DIGITEEE: ")
                if Player != "barco" and Player != "porta" and Player != "corpo" and Player != "grupo" : 
                    
                    t1 = time ()
                    Player= input("\n⚠️ Palavra incorreta! Digite novamente: ")
       
                    while Player != "barco" and Player != "porta" and Player != "corpo" and Player != "grupo" : 
                        t1 = time ()
                        Player= input("\n⚠️ Palavra incorreta! Digite novamente: ")
                           
                t2 = time ()
                TempoPalavras = t2 - t1
    
                sleep (1)
                print (f"▶ {NomesJogadores} digitou em {TempoPalavras:3.3} segundos! ")

                sleep (3)

                #Por fim, jogar com as sentenças.

                Sentenças = ("O rato roeu a roupa do rei de Roma." , "Rosas são vermelhas, borboletas são azuis." , "Tudo vale a pena se a alma não é pequena.", "Ontem eu recebi um telegrama.")
                Embaralhar = randint (0,3)
    
                print ("\n▶️ Agora, digite a sentença abaixo e dê enter no final:")
                sleep(2)

                print("\n\033[33mA sentença será --> {} ".format(Sentenças[Embaralhar]))
                sleep (1)
                print ("\033[37m❗❗❗Lembre-se: frases começam com letra MAIÚSCULA e terminam com PONTO FINAL.")
                sleep(5)
        
                t1 = time () #Começar a marcar o tempo de digitação do Player.
    
                Player= input("\n▶️ DIGITEEE: ")
                if Player != "O rato roeu a roupa do rei de Roma." and Player != "Rosas são vermelhas, borboletas são azuis." and Player != "Tudo vale a pena se a alma não é pequena." and Player != "Ontem eu recebi um telegrama." : 
                    t1 = time()
                    Player= input("\n⚠️ Sentença incorreta! Digite novamente: ")
       
                    while Player != "O rato roeu a roupa do rei de Roma." and Player != "Rosas são vermelhas, borboletas são azuis." and Player != "Tudo vale a pena se a alma não é pequena." and Player != "Ontem eu recebi um telegrama." :  
                        t1 = time()
                        Player= input("\n⚠️ Sentença incorreta! Digite novamente: ")
                                              
                t2 = time ()
                TempoSentença = t2 - t1
    
                sleep (1)
                print (f"▶ {NomesJogadores} digitou em {TempoSentença:3.3} segundos! \n")

                sleep (2)
                
                MediaTempo = (TempoNumeros + TempoLetras + TempoPalavras + TempoSentença ) / 4
                TempoIndividual.append (MediaTempo)
                j += 1

            Total = sum (TempoIndividual) / j #Média da soma de todas as vezes que o usuário jogou e se repetiu cada sentença.
            print (f"\n❗A média de tempo de {NomesJogadores} é : {Total:3.3} segundos. \n")
            TempoTotal.append (Total)
            i += 1
            
        #Nome[i] = TempoTotal [i] (Relacionar cada tempo com seu respectivo jogador).
        
        sleep (2) 
        print("\n\033[33m 🕓🕓 A média final do tempo de cada jogador foi: 🕓🕓")
        sleep (1)
        
        i = 0
        for i in range (len(Nomes)) :
            print (f"\033[37m                {Nomes[i]} | {TempoTotal[i]:3.3} \n")
            sleep(1)
        
        sleep (2)
        
        #Testar quais médias são maiores ou menores do que a outra, para formar o pódio.
        print ("\nA seguir, mostraremos o placar final do Jogo: ")
        sleep (2)

        print ("\n\033[33m 🏆🏆🏆 RESULTADO DO JOGO: 🏆🏆🏆 ") 
        sleep (2)
        
        MenorTempo = TempoTotal[0] #Quem tiver a menor média de tempo, ganha o jogo.
        i = 0                      
        for i in range (len(Nomes)) :
            for j in range (len(TempoTotal)) :
                if TempoTotal[i] <= MenorTempo :
                    Vencedor = Nomes [i]

        print (f"\n\033[37mO vencedor da partida é: ")
        sleep (2)
        print (f"🥇 {Vencedor} 🥇 ")
        sleep (1)
        print ("\n\033[33mPARABÉNS AO GANHADOR❗❗❗", "\n👏🎊👏🎊👏🎊👏🎊👏🎊")

        sleep (3)
        print ("\n\033[37mFIM DE JOGO❗ Você voltará para o Menu principal.")
        sleep (3) 


            

        

            
                   
    
            



