# 39) Crie a classe Partida com construtor que recebe pontos do time A e pontos do time B, e calcule automaticamente um atributo vencedor no construtor.

class Partida:
    def __init__(self,  pontos_time_a,  pontos_time_b):
        self.pontos_time_a = pontos_time_a
        self.pontos_time_b = pontos_time_b

        if pontos_time_a > pontos_time_b:
            self.vencedor = "Time A"
        elif pontos_time_b > pontos_time_a:
            self.vencedor = "Time B"
        else:
            self.vencedor = "Empate"
    
partida = Partida(10, 11)
print(partida.vencedor)




    
        