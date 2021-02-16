import sys
import os 
sys.path.append("caminho\\python\\")
from pymongo import MongoClient
import pandas as pd



class Banco:
    def __init__(self,host,porta):
        self.host = host
        self.porta = porta

    def conectar(self):
        conexao = MongoClient(self.host,self.porta)
        return conexao

    