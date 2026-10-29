import pandas as pd
import numpy as np

serie_amigos=["Pedro", "Morgan","Farfan","El Adrian","Jesse","Eliseo","Mario"]
print (" --- Serie listado de amigos   NC 0777")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
print (" --- Serie listado valor de billeteas MX   NC 0777")
amigos=pd.Series(serie_billetes)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
serie_bletras=["veinte","cincuenta","cien","docientos","quinientos","mil"]
print (" --- Serie listado nombre y valor de billeteas MX   NC 0777")
tablabilletes=pd.Series(serie_billetes, serie_bletras)
print(tablabilletes)
# diccionario dataframe
# diccionario de valor monedas  y nombre
print("datos de diccionario a DataFrame en pandas")
dic_monedas={
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_bletras" :["veinte","cincuenta","cien","docientos","quinientos","mil"]
}
tablabilletes=pd.DataFrame(dic_monedas,index=["A","B","C","D","E","F"])
print(tablabilletes)
print("Casa de cambio de Eliseo Nava NC 0777")