from dao.base_dao import BaseDao
from model.squad import Squad
from model.bd import Bd
from model.linguagem import Linguagem
from model.front import Front



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
                                ,sq.id
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
            linguagem = Linguagem(l[1], l[2])
            front = Front(l[3], l[4])
            bd = Bd(l[5], l[6])
            squad = Squad(l[0], linguagem.__dict__, front.__dict__, bd.__dict__, l[7])
            lista_squad.append(squad.__dict__)
        return lista_squad

    def buscar_por_id(self,id):
        comando_sql_buscar_id = f"""SELECT
                                sq.nome
                                ,l.linguagem
                                ,l.id
                                ,f.front
                                ,f.id
                                ,bd.bd
                                ,bd.id
                                ,sq.id
                                FROM squad as sq
                                JOIN linguagem as l
                                on sq.linguagem = l.id
                                JOIN front as f 
                                on sq.front = f.id
                                JOIN bd
                                on sq.bd = bd.id
                                where sq.id = {id}
                                """
        tupla = super().buscar_por_id(comando_sql_buscar_id)
        linguagem = Linguagem(tupla[1], tupla[2])
        front = Front(tupla[3], tupla[4])
        bd = Bd(tupla[5], tupla[6])
        squad = Squad(tupla[0], linguagem.__dict__, front.__dict__, bd.__dict__,tupla[7])
        return squad.__dict__
    
    def has_nome(self, nome_id):
        comando_sql_buscar_nome = f"SELECT * FROM squad where nome like '%{nome_id}%' limit 1 "
        a = super().buscar_por_id(comando_sql_buscar_nome)
        return (True if a else False)



        
        
            
            
