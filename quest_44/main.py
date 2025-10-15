# 44) Defina a classe Estatistica com construtor que recebe nome do jogador obrigatório e estatísticas opcionais via **kwargs (pontos, assistências, rebotes).

class Estatistica:
    def __init__(self, nome, **kwargs):
        self.nome = nome
        self.pontos = kwargs.get("pontos", 0)
        self.assistencias = kwargs.get("assistencias", 0)
        self.rebotes = kwargs.get("rebotes", 0)

    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"Pontos: {self.pontos}\n" 
                f"Assistências: {self.assistencias}\n"
                f"Rebotes: {self.rebotes}")
estatistica = Estatistica("João", pontos = 7, assistencias=4, rebotes = 3)
print(estatistica) 