from jogo_da_velha import JogadorHumano, JogoVelha, JogadorComputador

# Função para o usúario escolher o modo de jogo
def escolher_modo():
    while True:
        modo = input("Escolha o modo de jogo: 1 para dois jogadores humanos, 2 para jogar contra a máquina: ")
        if modo == "1":
            return JogadorHumano('X'), JogadorHumano('O')
        elif modo == "2":
            return JogadorHumano('X'), JogadorComputador('O', 'aleatoria')
        else:
            print("Modo inválido. Tente novamente")


# define se o jogador 2 será um robô ou um humano e começa o jogo
jogador1, jogador2 = escolher_modo()
jogo = JogoVelha(jogador1, jogador2)
jogo.jogar()