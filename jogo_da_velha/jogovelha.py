import random

class Tabuleiro:

    """
    
    Cria um tabuleiro 3x3 e imprime-o
    
    Cria um tabuleiro 3x3,o retorna como uma lista de listas,
    cria um metodo para marcar uma casa no tabuleiro,um para ver se
    todas as casas estão completas e depois imprime o tabuleiro

    parametros usados:

    self: essencial para o codigo rodar

    linha (int): usado para marcar a linha escolhida pelo jogador

    coluna (int): usado para marcar a coluna escolhida pelo jogador

    simbolo (str): usado para mostrar os simbolos 
    dos jogadores.

    """

    # cria um tabuleiro 3x3
    def __init__(self):
        self.casas = [[' ' for _ in range(3)] for _ in range(3)]

    # Retorna o tabuleiro atual
    def pegar_tabuleiro(self):
        return self.casas

    '''
    Marca uma casa no tabuleiro com o símbolo do jogador se a 
    casa estiver vazia, se não imprime que a casa já está marcada
    '''
    def marcar_casa(self, linha, coluna, simbolo):
        if self.casas[linha][coluna] == ' ':
            self.casas[linha][coluna] = simbolo
        else:
            print("Essa casa já está marcada!")

    # Imprime o tabuleiro na tela com separadores entre as casas
    def imprimir_tabuleiro(self):
        for linha in self.casas:
            print('|'.join(linha))
            print('-' * 5)
    
    # Verifica se todas as casas do tabuleiro estão preenchidas
    def esta_completo(self):
        return all(casa != ' ' for linha in self.casas for casa in linha)


class Jogador:

    """
    
    Cria uma classe jogador, o simbolo do jogador e a jogada.
    
    Cria uma classe "Jogador" que será a base para as subclasses a 
    seguir. Além disso cria um simbolo, que será atribuido para os
    jogadores 1 e 2. E por fim, cria um metodo "fazer_jogada"
    que será usada nas subclasses de jogador.

    parametros usados:

    self: essencial para o codigo rodar

    simbolo (str): usado para mostrar os simbolos 
    dos jogadores.

    tabuleiro: essencial para mostrar visualmente o que está acontecendo 
    ao jogador
    
    """

    def __init__(self, simbolo):
        self.simbolo = simbolo

    def fazer_jogada(self, tabuleiro):
        pass


class JogadorHumano(Jogador):

    """
    
    Cria a classe JogadorHumano que herda de Jogador, e define fazer_jogada
    
    Cria uma classe "JogadorHumano" que tem como base "Jogador".
    Nela é definido como irá se comportar o metodo "fazer_jogada"
    para quando o jogador 2 for um ser humano.

    parametros usados:

    self: essencial para o codigo rodar

    tabuleiro: essencial para mostrar visualmente o que está acontecendo 
    ao jogador
    
    """

    '''
    pergunta ao jogador a linha e a coluna no qual ele quer marcar,
    e se estiver livre, irá marcar o local com o simbolo
    do jogador.
    '''
    def fazer_jogada(self, tabuleiro):
        print(f"Jogador {self.simbolo}, é a sua vez.")
        linha = int(input("Digite a linha (digite 0, 1 ou 2): "))
        coluna = int(input("Digite a coluna (digite 0, 1 ou 2): "))
        tabuleiro.marcar_casa(linha, coluna, self.simbolo)


class JogadorComputador(Jogador):

    """
    
    Cria a classe JogadorComputador que herda de Jogador, e define fazer_jogada
    
    Cria uma classe "JogadorComputador" que tem como base "Jogador".
    Nela é definido como irá se comportar o metodo "fazer_jogada"
    para quando o jogador 2 for um Computador.

    parametros usados:

    self: essencial para o codigo rodar

    simbolo (str): usado para mostrar os simbolos 
    dos jogadores.

    tabuleiro: essencial para mostrar visualmente o que está acontecendo 
    ao jogador

    estrategia (str): usado para determinar a estrategia que será
    usada pelo computador

    """

    #cria a variavel estrategia, que será determinada em "fazer_jogada"
    def __init__(self, simbolo, estrategia):
        super().__init__(simbolo)
        self.estrategia = estrategia

    '''
    cria a estrategia aleatoria, onde o computador escolherá
    um número aleatorio entre 0 e 2 para a linha e a coluna,
    e se essa linha e coluna escolhida não estiver marcada,
    o computador irá escolher aquele local, se não, ele irá 
    escolher outro local aleatoriamente até conseguir achar um vazio.
    '''
    def fazer_jogada(self, tabuleiro):
        if self.estrategia == "aleatoria":
            while True:
                linha = random.randint(0, 2)
                coluna = random.randint(0, 2)
                if tabuleiro.pegar_tabuleiro()[linha][coluna] == ' ':
                    print("É a vez do computador jogar:")
                    tabuleiro.marcar_casa(linha, coluna, self.simbolo)
                    break


class JogoVelha:

    """
    
    Cria a classe JogoVelha, que será a parte principal do codigo.
    
    Cria uma classe "JogoVelha", ela quem irá checar qual o jogador
    atual e seu simbolo, imprimir o tabuleiro após cada jogada,
    checar se o jogo ja acabou e mostrar o ganhador da partida.

    parametros usados:

    self: essencial para o codigo rodar

    jogador1 : usado para definir o primeiro jogador, que será quem 
    terá controle do simbolo "X" 

    jogador2 : usado para definir o segundo jogador, que será quem 
    terá controle do simbolo "O" 
    
    """

    '''
    imprime o tabuleiro e define os dois jogadores,alem de definir
    o turno atual (usado para saber de qual jogador é a vez)
    '''
    def __init__(self, jogador1, jogador2):
        self.tabuleiro = Tabuleiro()
        self.jogadores = [jogador1, jogador2]
        self.turno = 0

    '''
    retorna e começa o turno do jogador atual, deixando o jogador
    fazer sua jogada, e após o jogador concluir sua jogada,
    o tabuleiro pós jogada será imprimido, depois, checa se o jogo
    acabou ou não, e se sim, mostra o ganhador da partida,
    e se ninguem ganhar, recomeça o processo de novo só que com o 
    próximo jogador.
    '''
    def jogar(self):
        while True:
            jogador_atual = self.jogador_atual()
            jogador_atual.fazer_jogada(self.tabuleiro)
            self.tabuleiro.imprimir_tabuleiro()
            resultado = self.checar_fim_de_jogo()
            if resultado:
                print(resultado)
                break
            self.turno = (self.turno + 1) % 2

    '''
    é usada para checar se o jogo acabou, checando todas as casas,
    e se o simbolo for igual em três casas consecutivas, diz que o
    jogador no qual tem as três casas com seu simbolo ganhou.
    '''
    def checar_fim_de_jogo(self):
        tab = self.tabuleiro.pegar_tabuleiro()
        for i in range(3):
            if tab[i][0] == tab[i][1] == tab[i][2] != ' ':
                return f"Jogador {tab[i][0]} ganhou!"
            if tab[0][i] == tab[1][i] == tab[2][i] != ' ':
                return f"Jogador {tab[0][i]} ganhou!"
        if tab[0][0] == tab[1][1] == tab[2][2] != ' ':
            return f"Jogador {tab[0][0]} ganhou!"
        if tab[0][2] == tab[1][1] == tab[2][0] != ' ':
            return f"Jogador {tab[0][2]} ganhou!"
        if self.tabuleiro.esta_completo():
            return "O jogo terminou em empate!"
        return None

    #vê qual é o jogador atual
    def jogador_atual(self):
        return self.jogadores[self.turno]