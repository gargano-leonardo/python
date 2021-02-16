import sys
import os 
sys.path.append("caminho\\python\\")
from infra.mongo import Banco as bd
import requests
from aplicacao.ambientes.config import Config as cf
from dominio.entidades import Entidades as en
from servico.servicos import *


def Main():
    #conexao = bd(cf.host,cf.porta).conectar()
    #cliente = cl(conexao).popula_clientes()
    #a = en.popula_clientes()
    #print(a)
    inicio_programa()

    url_oferta = "https://453449df-c194-440e-86cc-78f64ea612fb.mock.pstmn.io/offers"
    url_proposta = "https://453449df-c194-440e-86cc-78f64ea612fb.mock.pstmn.io/proposal"
    headers = {
        "Accept":"*/*",
        "User-Agent": "request",
    }
    
    id = '602b2642d7edf1c50d964a36'


    ofertas = requests.post(url_oferta,headers=headers, data= pesquisa_cliente(id) )

    ofertas_json = json.loads(ofertas.text)

    popula_ofertas(ofertas_json,id)

    oferta_escolhida = escolhe_oferta()
   
    resposta_proposta = verifica_proposta(ofertas_json["offers"][oferta_escolhida],id)

    dicio = {}
    dicio["oferta"] = ofertas_json["offers"][oferta_escolhida]
    dicio["cliente"] = pesquisa_cliente(id)

    proposta = requests.post(url_proposta,headers=headers, data= url_proposta )

    if resposta_proposta == True:
        print(proposta.text)
        print("Proposta salva para um envio posterior")
    else:
        print(resposta_proposta)
        
    

    


    

Main()



  