# 38) Crie a classe Bola com construtor que recebe marca e cor. Instancie duas bolas diferentes e imprima suas características.

class Bola:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def __str__(self):
        return f"Marca: {self.marca}, Cor: {self.cor}"
bola1 = Bola("Bola de Futebol de Campo Penalty", "Branca")
bola2 = Bola("Bola Campo Topper Slick", "Preta")

print(bola1)
print(bola2)
