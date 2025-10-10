# 40) Defina a classe Técnico com construtor que recebe nome e sobrenome, e crie automaticamente um atributo nome_completo concatenando ambos.

class Tecnico:
    def __init__(self, nome, sobrenome ):
        self.nome = nome
        self.sobrenome = sobrenome

    @property
    def nome_completo(self):
         return  f"{self.nome} {self.sobrenome}"
    
tecnico = Tecnico("Mateus", "dos Santos")
print(tecnico.nome_completo)
      