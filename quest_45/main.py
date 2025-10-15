# 45) Contexto: No basquete, uma temporada representa um período específico de competição de uma liga. 
# É importante documentar adequadamente essa classe para que outros programadores entendam facilmente seu propósito e como utilizá-la.
# O que você deve implementar: Classe Temporada com construtor que recebe: ano (obrigatório): O ano da temporada, liga (obrigatório): Nome da liga (ex: "NBA", "NBB")
# Docstring da classe deve explicar: O propósito da classe O que ela representa no contexto do basquete. Docstring do construtor __init__ deve conter:
# Descrição do que o construtor faz Lista de parâmetros com tipos e descrições Exemplo de uso básico. Requisitos técnicos: Use aspas triplas (""") para as docstrings
# Siga o formato padrão Python para documentação. Inclua informações sobre os tipos dos parâmetros. Mantenha as descrições claras e concisas. Por que isso é importante:
# Facilita a manutenção do código. Permite que outros desenvolvedores entendam rapidamente o propósito. Pode ser acessada via help(). Como verificar se está correto:
# Após criar a classe, use help(Temporada) no Python para verificar se a documentação aparece formatada corretamente.
# Dica: Lembre-se que docstrings são diferentes de comentários - elas ficam dentro da classe/método e podem ser acessadas programaticamente.

class Temporada:
    """
    Representa uma temporada de uma liga de basquete em um ano específico.

    Esta classe modela o conceito de temporada associando o ano da competição
    à liga correspondente, como "NBA" ou "NBB".

    Attributes:
        ano (int): Ano da temporada.
        liga (str): Nome da liga (ex: "NBA", "NBB").
    """

    def __init__(self, ano: int, liga: str) -> None:
        """
        Inicializa uma nova instância da classe Temporada.

        Args:
            ano (int): Ano da temporada.
            liga (str): Nome da liga (ex: "NBA", "NBB").

        Example:
            >>> temporada_nba_2025 = Temporada(2025, "NBA")
        """
        self.ano = ano
        self.liga = liga
    def __str__(self):
        return f"Temporada(ano={self.ano}, liga='{self.liga}')"
temporada1 = Temporada(2025, "NBA")
temporada2 = Temporada(2025, "NBB")
print(temporada1)
print(temporada2)

