from Usuario import Usuario
from Estatisticas import Estatisticas

class Conquista:
    titulo: str
    descricao: str
    dificuldade: str
    data: str
    usuario: Usuario
    estatisticas: Estatisticas

    def __init__(self, titulo: str, descricao: str, dificuldade: str, data: str, usuario: Usuario, estatisticas: Estatisticas):
        self.titulo = titulo
        self.descricao = descricao
        self.dificuldade = dificuldade
        self.data = data
        self.usuario = usuario
        self.estatisticas = estatisticas