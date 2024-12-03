from ConquistaDAO import ConquistaDAO
from Estatisticas import Estatisticas
from Conquista import Conquista
from Usuario import Usuario
import pprint


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class ConquistaCLI(SimpleCLI):
    def __init__(self):
        super().__init__()
        self.conquistaDAO = ConquistaDAO()
        self.add_command("create", self.create_conquista)
        self.add_command("read", self.read_conquista)
        self.add_command("readAll", self.read_all_conquistas)
        self.add_command("update", self.update_conquista)
        self.add_command("delete", self.delete_conquista)

    def create_conquista(self):
        titulo = input("Informe o titulo da conquista: ")
        descricao = input("Informe a descrição da conquista: ")
        data = input("Informe a data da conquista (YYYY-MM-DD): ")
        dificuldade = input("Informe a dificuldade da conquista:  ")

        nome_usuario = input("Informe o nome do usuário: ")
        localizacao_usuario = input("Informe a localização do usuário: ")
        idade_usuario = int(input("Informe o idade do usuário: "))
        usuario = Usuario(nome_usuario, localizacao_usuario, idade_usuario)

        tempo_conclusao = input("Informe o tempo de conclusão da conquista (ex: 1h 23m): ")
        tentativas = int(input("Informe o número de tentativas para concluir a conquista: "))
        estatisticas = Estatisticas(tempo_conclusao, tentativas)

        conquista = Conquista(titulo, descricao, dificuldade, data, usuario, estatisticas)

        self.conquistaDAO.createConquista(conquista)

    def read_conquista(self):
        id = input("Informe o ID da conquista: ")
        conquista = self.conquistaDAO.readConquistaById(id)
        if conquista:
            pprint.pprint(self.__conquistaToJSON(conquista))

    def read_all_conquistas(self):
        conquistas = self.conquistaDAO.readAllConquistas()
        if conquistas:
            for conquista in conquistas:
                pprint.pprint(self.__conquistaToJSON(conquista))

    def update_conquista(self):
        id = input("Informe o ID da conquista a ser atualizada: ")
        titulo = input("Informe o titulo atualizado da conquista: ")
        descricao_conquista = input("Informe a descrição atualizada da conquista: ")
        data = input("Informe a data da conquista (YYYY-MM-DD): ")
        dificuldade = input("Informe a dificuldade da conquista: ")

        nome_usuario = input("Informe o nome do usuário: ")
        localizacao_usuario = input("Informe a localização do usuário: ")
        idade_usuario = int(input("Informe o idade do usuário: "))
        usuario = Usuario(nome_usuario, localizacao_usuario, idade_usuario)

        tempo_conclusao = input("Informe o tempo para conclusão da conquista (ex: 1h 23m): ")
        tentativas = int(input("Informe o número de tentativas para concluir a conquista: "))
        estatisticas = Estatisticas(tempo_conclusao, tentativas)

        conquista = Conquista(titulo, descricao_conquista, data, dificuldade, usuario, estatisticas)

        self.conquistaDAO.updateConquista(id, conquista)

    def delete_conquista(self):
        id = input("Informe o ID da conquista a ser deletada: ")
        self.conquistaDAO.deleteConquista(id)

    def run(self):
        print("Sistema de Gerenciamento de Conquistas")
        print("Comandos disponíveis: create, read, readAll, update, delete, quit")
        super().run()

    def __conquistaToJSON(self, conquista: Conquista):
        dadosUsuario = {
            "titulo": conquista.usuario.nome,
            "localizacao": conquista.usuario.localizacao,
            "idade": conquista.usuario.idade
        }
        dadosEstatisticas = {
            "tempoConclusao": conquista.estatisticas.tempo_conclusao,
            "tentativas": conquista.estatisticas.tentativas
        }
        return {
            "titulo": conquista.titulo,
            "descricao": conquista.descricao,
            "data": conquista.data,
            "dificuldade": conquista.dificuldade,
            "usuario": dadosUsuario,
            "estatisticas": dadosEstatisticas
        }
