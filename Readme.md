<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>
# <h1 align=center> **PROYECTO INDIVIDUAL Nº1 📊** </h1>
# <h1 align=center> ![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas) ![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy) ![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib) ![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn) ![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn) ![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi) ![TextBlob](https://img.shields.io/badge/-TextBlob-333333?style=flat&logo=textblob) ![Render](https://img.shields.io/badge/-Render-333333?style=flat&logo=render)

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://greensqa.com/wp-content/uploads/2020/04/Machine-Learning-01.jpg"  height=300>
</p>

<hr>  

## **Descripción del problema (Contexto y rol a desarrollar)**

## Contexto

El presente proyecto tiene como objetivo desarrollar un sistema de recomendación de juegos basado en la plataforma Steam. El sistema estará compuesto por un Producto Mínimo Viable (MVP) que incluirá:

API: Una interfaz de programación de aplicaciones (API) que permitirá a los usuarios obtener recomendaciones de juegos.
Modelo de Machine Learning: Un modelo de Machine Learning que se encargará de generar las recomendaciones.
Funciones extras: Funciones adicionales relacionadas con Steam, como la búsqueda de juegos, la obtención de información de juegos y la gestión de la biblioteca de juegos.

<p align="center">
<img src="https://www.servicetonic.com/wp-content/uploads/2020/10/API-Interface-Servicetonic.png"  height=500>
</p>

## **Descripcion del proyecto**

Datasets: En esta carpeta encontraremos todo lo que se necesita para comenzar! Hemos preprocesado cuidadosamente los conjuntos de datos utilizando técnicas ETL (Extracción, Transformación y Carga) para asegurarnos de que funcionen a la perfección tanto en FastAPI como en Render.

EDA: Los datos ya están limpios y relucientes, listos para ser explorados. Es hora de sumergirnos en ellos y descubrir los secretos que esconden.
El objetivo es obtener una comprensión profunda de los datos, identificar oportunidades y tomar decisiones estratégicas basadas en evidencia.

Funciones.py/Recomendacion.py: Estas albergan las funciones que dan vida a la API, proporcionando a los usuarios los datos y recomendaciones que necesitan, se podria decir que es el cerebro de la operación.

Pruebas_Recomendaciones/Pruebas_Funciones: Se muestra las pruebas que se realizaron para verificar el resultado de las funciones.

main.py es el archivo central que da vida a la API FastAPI. Es el maestro de ceremonias, el que coordina las diferentes funciones y las expone al mundo a través de endpoints bien definidos.
es una pieza fundamental del sistema de recomendación, ya que permite que los usuarios interactúen con la API y obtengan las recomendaciones que necesita
requirements.txt: El archivo que lista las bibliotecas de Python necesarias para ejecutar el proyecto.

*disponibilizar los datos de la empresa usando el framework ***FastAPI***. Las consultas que propones son las siguientes:

<sub> Debes crear las siguientes funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).<sub/>

## **Desarrollo API**

Para el desarrolo de la API se utiliza el framework FastAPI, creando las siguientes funciones solicitadas:

+ Def **developer( *desarrollador : str )**: Devuelve la cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.

+ Def **userdata( *User_id : str )**: Devuelve la cantidad de dinero gastado por el usuario y el porcentaje de recomendación 

+ Def **UserForGenre( *genero : str )**: Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.

+ Def **best_developer_year( *año : int )**: Devuelve el top 3 de desarrolladores con juegos mas recomendados por usuarios para el año dado.

+ Def **developer_reviews_analysis( *desarrolladora : str )**: Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador una lista con la cantidad total de registros de reseñas de usuarios como valor positivo o negativo.
<br/>


**`Modelo de aprendizaje automático`**: 

El EDA ha sido nuestro faro en este viaje.  Gracias a él, ahora tenemos una comprensión profunda de los datos y estamos listos para dar el siguiente paso: entrenar nuestro modelo de Machine Learning.
El modelo de recomendación está listo para brillar. ✨ Se ha creado a partir de la data steam_games, utilizando los item_id, géneros y nombres de videojuegos

+ Def **recomendacion_juego( *item_id : int )**: Esta función recibira como parametro el "id" de un titulo de juego y devuelve una lista con 5 juegos recomendacos similares al ingresado tomando como base de similitus el genero. 
<br/>

**Video**  
  
Link: https://youtu.be/lUm7BejtsRE
<br/>  
**Deploy**  
  
Link: https://steam-g.onrender.com/docs  
<br/>  

Linkedin: Luis Mary Gaince



