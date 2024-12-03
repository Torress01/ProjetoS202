from Database import Database
from Estatisticas import Estatisticas
from Usuario import Usuario
from Conquista import Conquista
from bson.objectid import ObjectId


class ConquistaDAO:

    def __init__(self):
        self.db = Database("ProjetoFinal", "Conquistas")

    def createConquista(self, conquista: Conquista):
        conquistaJSON = self.__conquistaToJSON(conquista)
        try:
            res = self.db.collection.insert_one(conquistaJSON)
            print(f"Conquista criada com sucesso com o id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar a conquista: {e}")
            return None

    def readConquistaById(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})

            if res:
                print("Conquista encontrada:")
                print(f"Título: {res['titulo']}")
                print(f"Descrição: {res['descricao']}")
                print(f"Dificuldade: {res['dificuldade']}")
                print(f"Data: {res['data']}")

                print("Usuário:")
                print(f"  Nome: {res['usuario']['nome']}")
                print(f"  Localização: {res['usuario']['localizacao']}")
                print(f"  Idade: {res['usuario']['idade']}")

                print("Estatísticas:")
                print(f"  Tempo de Conclusão: {res['estatisticas']['tempoConclusao']}")
                print(f"  Tentativas: {res['estatisticas']['tentativas']}")

            else:
                print("Conquista não encontrada!")
                return None
        except Exception as e:
            print(f"Ocorreu um erro ao buscar a conquista: {e}")
            return None

    def readAllConquistas(self):
        try:
            res = self.db.collection.find()
            conquistas = [self.__criaConquista(conquista) for conquista in res]
            if conquistas:
                print("Lista de Conquistas:")
                for idx, conquista in enumerate(conquistas, 1):
                    print(f"\nConquista #{idx}")
                    print(f"Título: {conquista.titulo}")
                    print(f"Descrição: {conquista.descricao}")
                    print(f"Dificuldade: {conquista.dificuldade}")
                    print(f"Data: {conquista.data}")
                    print(f"Usuário: {conquista.usuario.nome}")
                    print(f"Localização: {conquista.usuario.localizacao}")
                    print(f"Idade: {conquista.usuario.idade}")
                    print(f"Tempo de Conclusão: {conquista.estatisticas.tempo_conclusao}")
                    print(f"Tentativas: {conquista.estatisticas.tentativas}")
            else:
                print("Nenhuma conquista encontrada.")

        except Exception as e:
            print(f"Ocorreu um erro ao buscar as conquistas: {e}")
            return None

    def updateConquista(self, id: str, conquista: Conquista):
        conquistaJSON = self.__conquistaToJSON(conquista)
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": conquistaJSON})
            print(f"Conquista atualizada: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar a conquista: {e}")
            return None

    def deleteConquista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Conquista excluída: {res.deleted_count} documento(s) excluído(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar a conquista: {e}")
            return None

    def __conquistaToJSON(self, conquista: Conquista):
        usuarioJSON = {
            "nome": conquista.usuario.nome,
            "localizacao": conquista.usuario.localizacao,
            "idade": conquista.usuario.idade
        }
        estatisticasJSON = {
            "tempoConclusao": conquista.estatisticas.tempo_conclusao,
            "tentativas": conquista.estatisticas.tentativas
        }
        return {
            "titulo": conquista.titulo,
            "descricao": conquista.descricao,
            "dificuldade": conquista.dificuldade,
            "data": conquista.data,
            "usuario": usuarioJSON,
            "estatisticas": estatisticasJSON
        }

    def __criaConquista(self, conquistaJSON):
        usuario = Usuario(
            conquistaJSON["usuario"]["nome"],
            conquistaJSON["usuario"]["localizacao"],
            conquistaJSON["usuario"]["idade"]
        )
        estatisticas = Estatisticas(
            conquistaJSON["estatisticas"]["tempoConclusao"],
            conquistaJSON["estatisticas"]["tentativas"]
        )
        return Conquista(
            conquistaJSON["titulo"],
            conquistaJSON["descricao"],
            conquistaJSON["dificuldade"],
            conquistaJSON["data"],
            usuario,
            estatisticas
        )
