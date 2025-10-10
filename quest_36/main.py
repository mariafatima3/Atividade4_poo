# 36) Crie a classe Jogador com um construtor que recebe o nome do jogador e armazena em um atributo. Instancie um objeto com o nome "Michael Jordan".

class Jogador:
    def __init__(self, nome):
        self.nome = nome


jogador = Jogador( "Michael Jordan")
print(jogador.nome)

