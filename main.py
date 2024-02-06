
from fastapi import FastAPI, Path, HTTPException
import pandas as pd

app=FastAPI()

from Recomendaciones import recomendacion_juego
from Funciones import developer_data, userdata, UserForGenre, best_developer_year, developer_reviews_analysis

df_reviews = pd.read_csv("Datasets/reviews_ETL.csv")
df_items = pd.read_csv("Datasets/user_items_EtL.csv")
df_steam_games = pd.read_csv("Datasets/steam_games_API.csv")

#http://127.0.0.1:8000/

@app.get('/developerinfo/{desarrollador}')
def developer_info(desarrollador: str):
    resultado: pd.DataFrame = developer_data(desarrollador)
    return resultado.to_dict(orient='records')

@app.get("/userdata/{user_id}")
async def user_data(user_id: str):
    resultado1 = userdata(user_id)
    return resultado1

@app.get("/usergenre/{genero}")
async def user_genre(genero: str):
    result = UserForGenre(genero)
    return result

@app.get("/bestdeveloper/{anio}")
def get_best_developers(year: int):
    resultado = best_developer_year(year)
    return {"Top 3 desarrolladores para el año {}: ".format(year): resultado}

@app.get('/developerreviews/{desarrolladora}')
def developer(desarrolladora: str):
    resultado = developer_reviews_analysis(desarrolladora)
    return resultado

@app.get("/recomendacion_juego/{id_producto}")
async def get_recomendacion_juego(id_producto: int):
    result = recomendacion_juego(id_producto) 
    return {"Recomendaciones": result}


