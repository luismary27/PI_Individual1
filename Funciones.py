import pandas as pd

df_reviews = pd.read_csv("Datasets/reviews_ETL.csv")
df_items = pd.read_csv("Datasets/user_items_EtL.csv")
df_steam_games = pd.read_csv("Datasets/steam_games_API.csv")

def developer_data(desarrollador: str):
    df_dev = df_steam_games.loc[:,['developer', 'item_id', 'price','release_date']]#Sacamos del Dataframe las columnas a necesitar
    dev_desarrolladora = df_dev[df_dev['developer'] == desarrollador]#Se filtra el DataFrame para los juegos de la empresa desarrolladora especifica
    juegos_total = dev_desarrolladora.groupby('release_date').size().reset_index(name='Cantidad de Items')#Agrupamos por año y cuenta la cantidad de juegos
    juegos_free = dev_desarrolladora[dev_desarrolladora['price'] == 0]#Filtra los juegos free
    juegos_freeanio = juegos_free.groupby('release_date').size().reset_index(name='Juegos_cantidad')#Agrupa los juegos free por año y cuenta el total
    resultado = pd.merge(juegos_total,juegos_freeanio, on='release_date', how='left')#Junta los datos de juegos totales y juegos free por año
    resultado['Juegos_cantidad'].fillna(0, inplace=True)#En los valores nulos en juegos_cantidad se coloca 0
    resultado['porcentaje_juegos_gratuitos'] = (resultado['Juegos_cantidad'] / resultado['Cantidad de Items']) * 100#Se calcula el porcentaje de juegos gratuitos por año
    resultado.drop(columns='Juegos_cantidad', inplace=True)#Se elimian la columna 'juegos_cantidad'
    resultado.rename(columns={'release_date': 'Año', 'porcentaje_juegos_gratuitos': 'Contenido Free'}, inplace=True)#Renombramos las columnas como en las indicaciones
    resultado['Cantidad de Items'] = resultado['Cantidad de Items'].astype(int)#Convierte la columna 'Cantidad de Items' a enteros 'Contenido Free' a flotantes
    resultado['Contenido Free'] = resultado['Contenido Free'].astype(float)#'Contenido Free' a flotantes
    #Convierte el DataFrame a una lista de diccionarios como se indica
    resultado_final_dev = resultado
    return resultado_final_dev


def userdata(user_id: str):
  user_id = str(user_id)# Convertimos el user_id a cadena para asegurar coincidencia en las comparaciones
  user_compras = df_items[df_items['user_id'] == user_id]# Filtrar las compras del usuario en df_items
  user_compras = pd.merge(user_compras, df_steam_games, left_on='item_id', right_on='item_id', how='inner')# Combinamos la información de las compras con los datos de los juegos en df_steam_games
  user_compras['price'] = pd.to_numeric(user_compras['price'], errors='coerce')# Asegurarnos que "price" sea tratada como tipo numerico (para evitar errores de suma)
  total_price = round(user_compras['price'].sum(), 2)# Calculamos el monto de gasto total por usuarios
  user_reviews = df_reviews[(df_reviews['user_id'] == user_id) & (df_reviews['item_id'].isin(user_compras['item_id']))] # Se filtran las revisiones del usuario en df_reviews
  recomendacion_posi = (user_reviews['recommend'].sum() / float(len(user_reviews))) * 100 if len(user_reviews) > 0 else 0# Se calcula el porcentaje de recomendaciones positiva
  items_count = len(user_compras)# Calcular la cantidad de ítems comprados
  user_name = user_compras['user_id'].iloc[0] if not user_compras.empty else None# Extraer el nombre del usuario

  # Devolver las estadísticas
  return {
    'Usuarios': user_name,
    'Dinero gastado': total_price,
    'Porcentaje de recomendación': recomendacion_posi,
    'Cantidad de Ítems': items_count
  }


def UserForGenre(genero: str):
    filtro_steam = df_steam_games[df_steam_games["genres"].str.contains(genero, case=False, na=False)]#Filtramos el df_steam_games por el género
    filtro_items = df_items[df_items["item_id"].isin(filtro_steam["item_id"])][["item_id", "user_id", "playtime_forever"]]#Filtra df_items por los juegos del género y selecciona las columnas necesarias
    #Renombrar la columna "id" a "item_id" en filtro_steam
    filtro_steam = filtro_steam.rename(columns={"item_id": "item_id"})
    filtro_items = filtro_items.merge(filtro_steam[["item_id", "release_date"]], how="inner", on="item_id")#Une los DataFrames por "item_id"
    #Convierte "release_date" a tipo fecha y hora
    try:
        filtro_items["release_date"] = pd.to_datetime(filtro_items["release_date"], errors="coerce")
    except ValueError:
        return {"Error": "No se pueden convertir todas las fechas 'release_date' a un tipo de fecha y hora."}
    resultado_df1= filtro_items.groupby(["user_id", filtro_items["release_date"].dt.year])["playtime_forever"].sum().reset_index()#Calcula las horas jugadas por año y usuario
    max_user = resultado_df1.loc[resultado_df1["playtime_forever"].idxmax()]# Obtiene el usuario con más horas jugadas
    resultado_df1["playtime_forever"] = (resultado_df1["playtime_forever"] / 3600).round(0)# Convierte las horas jugadas a formato adecuado
    #Acumula las horas jugadas por año
    horas_acumuladas = resultado_df1.groupby("release_date")["playtime_forever"].sum().reset_index()
    horas_acumuladas = horas_acumuladas.rename(columns={"release_date": "Año", "playtime_forever": "Horas"})
    horas_final= horas_acumuladas.to_dict(orient="records")
    return {
      "Usuario con más horas jugadas para el género " + genero: max_user["user_id"],
       "Horas jugadas":horas_final ,
    }


def best_developer_year(year: int):
  df_steam_games['release_date'] = df_steam_games['release_date'].astype(str)#Convierte la columna release_date a cadena de texto
  juegos_del_año = df_steam_games[df_steam_games['release_date'].str[:4] == str(year)]#Filtramos los juegos del año especificado
  juegos_recomendados = pd.merge(juegos_del_año, df_reviews, left_on="item_id", right_on="item_id", how="inner")#Se Combinan los DataFrames para obtener juegos recomendados
  juegos_recomendados = juegos_recomendados[(juegos_recomendados["recommend"] == True) & (juegos_recomendados["sentiment_analisis"] == 2)] #Filtramos juegos recomendados con comentarios positivo
  #Agrupamos por desarrollador y contamos las recomendaciones
  desarrolladores_recomendados = juegos_recomendados["developer"].value_counts().reset_index()
  desarrolladores_recomendados.columns = ["developer", "recommend_count"]
  top_desarrolladores = desarrolladores_recomendados.nlargest(3, "recommend_count")#Ordenamos por recomendaciones y tomar los 3 mejores
  #Formatear el resultado como una lista de diccionarios
  resultado = [
    {"Puesto {}: {}".format(i + 1, row["developer"]): row["recommend_count"]}
    for i, row in top_desarrolladores.iterrows()
  ]

  return resultado

def developer_reviews_analysis(desarrolladora: str):
    juegos_desarrollador = df_steam_games[df_steam_games["developer"] == desarrolladora]#Filtramoss los juegos del desarrollador
    reseñas_desarrollador = df_reviews[df_reviews["item_id"].isin(juegos_desarrollador["item_id"])]#Filtramos las reseñas por los juegos del desarrollador
    # Cuenta las reseñas con sentimiento positivo y negativo
    sentimiento_positivo = reseñas_desarrollador[reseñas_desarrollador["sentiment_analisis"] == 2].shape[0]
    sentimiento_negativo = reseñas_desarrollador[reseñas_desarrollador["sentiment_analisis"] == 0].shape[0]
    # Crea el diccionario de resultados
    resultado = {
        desarrolladora: {
            "Positive": sentimiento_positivo,
            "Negative": sentimiento_negativo,
        }
    }

    return resultado 

