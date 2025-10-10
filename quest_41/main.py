# 41) Crie a classe Cestinha com construtor que recebe nome do jogador e opcionalmente a quantidade de pontos (padrão 0).
class  Cestinha:
    def __init__(self, nome, pontos=0):
        self.nome = nome
        self.pontos = pontos

    def __str__(self):
        return f"Nome: {self.nome}, pontos: {self.pontos}"
cestinha1 = Cestinha("Lucas")
cestinha2 = Cestinha("Vitor", 2)
print(cestinha1)
print(cestinha2)