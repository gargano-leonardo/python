import sys
import os 
sys.path.append("caminho\\python\\")
from dominio.entidades import Entidades as ent
from bson.objectid import ObjectId
import json
import random
from datetime import datetime





def pesquisa_cliente(id):
    
    cliente = ent.banco.Clientes.find_one({"_id": ObjectId(id)})
    del cliente["_id"]
    return cliente


def inicio_programa():
    ent.popula_clientes()

def popula_ofertas(json_ofertas, id):
        ofertas = ent.banco.Ofertas
        dicio = {}
        agora = datetime.now()
        data = agora.strftime("%Y-%m-%d %H:%M")
        dicio['date'] = data
        dicio['id_cliente'] = ObjectId(id)
        dicio['offers'] = json_ofertas["offers"]
        
        try:
            ofertas.insert(dicio)
            return "sucesso"
        except:
            return "erro ao popular oferta"

def escolhe_oferta():
    n = random.randint(0,4)
    return n 

def verifica_proposta(oferta,id):
    cliente = pesquisa_cliente(id)
    proposta = ent.banco.Proposta 
    verifica = ent.banco.Proposta.find_one({"client.cpf": cliente["cpf"],
    "client.full_name": cliente["full_name"], 
    "offers.partner_id": oferta["partner_id"],
     "offers.partner_name": oferta["partner_name"],
      "offers.value": oferta["value"],
     "offers.installments": oferta["installments"],
      "offers.tax_rate_percent_montly": oferta["tax_rate_percent_montly"],
      "offers.total_value": oferta["total_value"]
       })
    
   
    if verifica == None: 
        try:
            agora = datetime.now()
            data = agora.strftime("%Y-%m-%d %H:%M")
            dicio = {}
            dicio['date'] = data
            dicio['client'] = cliente
            dicio['offers'] = oferta
            proposta.insert(dicio)
            return True
        except:
            return "erro ao salvar proposta"
    else:
        return "cliente ja enviou uma proposta para essa oferta"
    
    






    