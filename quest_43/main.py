# 43) Crie a classe Escalacao com construtor que recebe o nome do técnico e uma quantidade variável de jogadores usando *args.

class Escalacao:
    def __init__(self, tecnico, *jogadores):
        self.tecnico = tecnico 
        self.membros = list(jogadores)

    def __str__(self):
        return f"Técnico: {self.tecnico}, Jogadores: {', '.join(self.membros)}"
    
escalacao = Escalacao( "Bruno", "Carlos", "João", "Lucas", "José", "Vitor")
print(escalacao)    