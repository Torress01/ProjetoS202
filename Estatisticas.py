class Estatisticas:
    tempo_conclusao: str
    tentativas: int

    def __init__(self, tempo_conclusao: str, tentativas: int):
        self.tempo_conclusao = tempo_conclusao
        self.tentativas = tentativas
