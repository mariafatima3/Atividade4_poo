# 37) Defina a classe Quadra com construtor que recebe largura e comprimento da quadra. Crie uma instância com dimensões 28x15 metros.


class Quadra:
  def __init__(self,largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento


quadra = Quadra(28, 15)
print(f"Largura: {quadra.largura} metros")
print(f"Comprimento: {quadra.comprimento} metros")
