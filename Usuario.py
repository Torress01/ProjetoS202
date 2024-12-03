class Usuario:
    nome: str
    localizacao: str
    idade: int

    def __init__(self, nome: str, localizacao: str, idade: int):
        self.nome = nome
        self.localizacao = localizacao
        self.idade = idade
