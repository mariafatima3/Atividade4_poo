# 42) Defina a classe Arena com construtor que recebe nome (obrigatório), capacidade (padrão 10000) e cidade (padrão "Não informada").

class Arena:
    def __init__(self, nome, capacidade=10000, cidade="Não informada"):
        self.nome = nome
        self.capacidade = capacidade
        self.cidade = cidade

    def __str__(self):
        return f"Nome: {self.nome}, Capacidade: {self.capacidade}, Cidade: {self.cidade}"
arena1 = Arena("Maracanã")
arena2 = Arena("Castelão", 63903, "Fortaleza")
print(arena1)
print(arena2)