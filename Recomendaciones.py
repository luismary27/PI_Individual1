#importamos librerias
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer

#importamos el dataset
df_modelo = pd.read_csv('Datasets/modelo.csv')

#Convertimos los datos
df_modelo['item_id']=df_modelo['item_id'].astype('string')

df_modelo1= pd.get_dummies(df_modelo, columns=["genres"], prefix="")#Realizar codificación one-hot en la columna 'genres' 
df_modelo1.replace({True: 1, False: 0}, inplace=True)                # y reemplazamos los valores booleanos con 1 y 0

df_modelo2= df_modelo1.groupby(["item_id","app_name"]).sum().reset_index()#Resumimos los datos y obtenemos una vista general de las tendencias

df_modelo2['item_id']=df_modelo2['item_id'].astype('string')#Convertimos la columna 'item_id' nuevamente a string y luego a entero:
df_modelo2['item_id']=df_modelo2['item_id'].astype('int')

def recomendacion_juego(item_id):
    juego_elegido= df_modelo2[df_modelo2['item_id'] == item_id] #Filtramos el juego e igualarlo a su ID
    # devolver error en caso de vacio
    if juego_elegido.empty:
        return "El juego con el ID especificado no existe en la base de datos."
    
    similitudes= cosine_similarity(df_modelo2.iloc[:,3:])#Calculamos la matriz de similitud coseno 
    similitudes_count = similitudes[df_modelo2[df_modelo2['item_id'] == item_id].index[0]] #Calculamos la similitud del juego que se ingresa con otros juegos del dataframe
    juegos_similares = similitudes_count.argsort()[::-1][1:6]#Se calcula los índices de los juegos más similares excluyendo al que eligio
    #Obtenemos los nombres de los juegos 5 recomendados
    juegos_recomendados = df_modelo2.iloc[juegos_similares]['app_name']
    
    return {
        "Juegos_recomendados" :juegos_recomendados}
