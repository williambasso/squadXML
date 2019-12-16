from dao.base_dao import BaseDao
from model.squad import Squad


class SquadDao(BaseDao):
    def inserir(self, squad: Squad):
        comando_sql_insert = f"""
                                INSERT INTO squad
                                (nome, linguagem, bd, front)
                                VALUES
                                (
                                    '{squad.nome}'
                                    ,'{squad.linguagem}'
                                    ,'{squad.bd}'
                                    ,'{squad.front}'
                                )
                                """
        return super().inserir(comando_sql_insert)

    # def alterar(self, squad: Squad):
    #     comando_sql_alterar = f"""
    #                         UPDATE squad
    #                         SET
    #                             nome = '{squad.nome}',
    #                             linguagem = '{squad.linguagem}',
    #                             bd = '{squad.bd}',
    #                             front = '{squad.front}'
    #                         WHERE ID = {squad.id}
    #                         """
    #     super().alterar(comando_sql_alterar)

    def deletar(self, id):
        comando_sql_deletar = f"""
                                DELETE FROM squad 
                                WHERE ID = {id}
                            """
        super().deletar(comando_sql_deletar)
        return "Deletou quiridu"

    def listar(self):
        lista_squad = []
        comando_sql_listar = """SELECT
                                sq.nome
                                ,l.linguagem
                                ,l.id
                                ,f.front
                                ,f.id
                                ,bd.bd
                                ,bd.id
                                FROM squad as sq
                                JOIN linguagem as l
                                on sq.linguagem = l.id
                                JOIN front as f 
                                on sq.front = f.id
                                JOIN bd
                                on sq.bd = bd.id
                            """
        lista_tuplas = super().listar(comando_sql_listar)
        for l in lista_tuplas:
            squad = Squad()
