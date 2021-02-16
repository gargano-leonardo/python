import sys
import os 
sys.path.append("caminho\\python\\")


import pandas as pd

from datetime import datetime
import os
from infra.mongo import Banco as bd
from aplicacao.ambientes.config import Config as cf
from bson.objectid import ObjectId

class Entidades:
    def __init__(self):
       
        pass
    conexao = bd(cf.host,cf.porta).conectar()
    banco = conexao.Entidades
    
    
    def cliente_inicio():
        
        dicio = {
            "_id" : ObjectId("602b2642d7edf1c50d964a36"),
            "cpf" : "566.050.380-29",
            "full_name" : "Renata Sophia Luiza Costa",
            "date_birth" : "17/12/1990",
            "email" : "renatasophialuizacosta__renatasophialuizacosta@gmeil.com",
            "phone" : "(84) 99294-4912",
            "net_salary" : 2000
        }
        clientes = Entidades.banco.Clientes
        verifica = clientes.find_one({"_id":  ObjectId("602b2642d7edf1c50d964a36")})
        if verifica:
            try:
                
                clientes.insert_one(dicio)
                return "sucesso"
            except:
                return "erro ao popular clientes"

    def popula_clientes():
        Entidades.cliente_inicio()
        clientes = Entidades.banco.Clientes


        df = pd.read_csv(os.getcwd() + "\\infra\\popula_bd.csv", sep=";")
        df.reset_index(drop=True)#inplace=True)
        try:
            data_dict = df.to_dict("records")
            clientes.insert_many(data_dict)
            return "sucesso"
        except:
            return "erro ao popular clientes"

    
    

    






