from random import randint
from time import sleep

#Mensagem de boas-vindas
def bem_Vindo():
    print('''Seja Bem-Vindo(a).
Aqui você irá jogar o famoso Jokempô, mais conhecido como Pedra, Papel, Tesoura. Então relaxa e agachar, fique bem tranquilo aí e se divirta ;)\n''')

#Função para escolher o modo de jogo (No momento só terá 2)
def modo_de_Jogo():

    print("Agora escolha o modo de jogo que queira jogar:\n[1] Modo Rápido (Uma rodada e acabou)\n[2] Modo Multiplas rodadas (Você joga um total de 5 rodadas)\n")
    print("Notas do Desenvolvedor: Mais para frente colocarei para escolher a quantidade de rodadas\n")

    while True:
        try:
            opcaoDeModo = int(input("Esolha o modo de Jogo que deseja \n-> "))
            
            if opcaoDeModo == 1:
                return 1
                # break
            else:
                return 2
                # break
            
        except ValueError:
            print("Insira um valor inteiro\n")
    
#função para caso o jogador queira jogar novamente
def jogar_novamente():
    while True:
        jogar = input("Quer continuar jogando? (S/N) -> ").lower()
        if jogar in ['s', 'sim']:
            jogo()

        elif jogar in ['n', 'não']:
            print("Espero te ver aqui novamente :)")
            break

        else:
            print("Entrada inválida. Digite 'S'/'Sim' para sim ou 'N'/'Não' para não.")

#Função do modo de jogo que está pronto
def jogo(qntdDeRodadas):

    #Contar as rodadas
    contadorDeRodadas = 0
    #Contar os pontos do Jogador
    pontosJ = 0
    #Contar os pontos do Computador
    pontosC = 0
    while True:
        
        #verificação do contador para encerrar o loop do jogos
        if contadorDeRodadas == qntdDeRodadas:
            break
        
        #Para armazenar em indices para manipular qual será a escolha baseada no número
        jokempo = ["Pedra", "Papel", "Tesoura"]

        #Gerar um número de 0 a 2 para lançar qual foi a escolha
        computador = randint(0,2)
        
        #Para pedir que o usuário coloque a informação que está sendo pedida 
        try:
            jogador = int(input("\nEscolha uma opção entre essas: \n[1]Pedra \n[2]Papel \n[3]Tesoura \n-> "))
        except ValueError:
            print("Escolha entre uma dessas opções numeradas\n")
        
        #Verificação se o jogador inseriu um número dentro do intervalo
        if 1 <= jogador <= 3:
            
            #Esse "Jogador -= 1" é para entra no intervalo de indice da lista "jokempo"
            jogador -= 1

            #Verificar a condição de empate
            if jogador == computador:
                sleep(0.5)
                print("")
                print("-="*11)
                print(f"{jokempo[jogador]}\n{jokempo[computador]}")
                print("-="*11)
                sleep(0.5)
                print(f"Empate!!\n")

                #Contador de rodadas aumentando para poder parar o loop
                contadorDeRodadas += 1

                
                
            #Verifica a condição de vitória do jogador
            elif(jogador == 0 and computador == 2) or \
                (jogador == 1 and computador == 0) or \
                (jogador == 2 and computador == 1):
                sleep(0.5)
                print("")
                print("-="*11)
                print(f"{jokempo[jogador]}\n{jokempo[computador]}")
                print("-="*11)
                sleep(0.5)
                print("Você venceu!!!!\n")

                #Contador de rodadas aumentando para poder parar o loop
                contadorDeRodadas += 1
                
                #Contar os pontos do Jogador
                pontosJ += 1
            
            #Verifica a condição de derrota do jogador
            else:
                sleep(0.5)
                print("")
                print("-="*11)
                print(f"{jokempo[jogador]}\n{jokempo[computador]}")
                print("-="*11)
                sleep(0.5)
                print("Que pena, você perdeu! :(\n")

                #Contador de rodadas aumentando para poder parar o loop
                contadorDeRodadas += 1
                
                #Contar os pontos do Computador
                pontosC += 1

            #Condição para verificar empate para uma rodada de desempate
            if contadorDeRodadas == 3 and pontosC == pontosJ:
                print(f"Jogador/Computador \n{pontosJ}     /  {pontosC}")
                print("Empates não são permitidos aqui!!")
                contadorDeRodadas -= 1

        #Mensagem para o usuário inserir um número dentro do intervalo
        else:
            print("\nInsira um número dentro do intervalo entre 1 e 3")

    #Placar do Jogador e do Computador
    print(f"Jogador/Computador \n{pontosJ}     /  {pontosC}")

def main():
    bem_Vindo()

    while True:
        modo = modo_de_Jogo()
        if modo == 1:
            jogo(1)

        elif modo == 2:
            jogo(5)

        else:
            print("Modo de jogo inválido")

        if not jogar_novamente():
            break


if __name__ == "__main__":
    main()

