from typing import Union
import unicodedata as unicodedata
from fastapi import FastAPI
import pandas as pd
from pandas import read_csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = FastAPI()

df = read_csv('df_transformado.csv')

ml=df.sample(n=2000, random_state=42) 

tfidf= TfidfVectorizer(stop_words = 'english') 
ml['overview'] = ml['overview'].fillna('') 
tfidf_matrix = tfidf.fit_transform(ml['overview']) 
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
ml.drop_duplicates(inplace=True)
ml = ml.reset_index(drop=True)
indices = pd.Series(ml.index, index=ml['title'])

@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes):
    months_translated= {
    'enero': 'January',
    'febrero': 'February',
    'marzo': 'March',
    'abril': 'April',
    'mayo': 'May',
    'junio': 'June',
    'julio': 'July',
    'agosto': 'August',
    'septiembre': 'September',
    'octubre': 'October',
    'noviembre': 'November',
    'diciembre': 'December'}  
    fechas = pd.to_datetime(df['release_date'], format= '%Y-%m-%d')
    n_mes = fechas[fechas.dt.strftime('%B').str.capitalize() == months_translated[str(mes).lower()]]
    respuesta = n_mes.shape[0]
    return {'mes':mes, 'cantidad':respuesta}

@app.get('/peliculas_dia/{dia}')
def peliculas_dia(dia):
    day_translated= {
    'lunes': 'Monday',
    'martes': 'Tuesday',
    'miercoles': 'Wednesday',
    'jueves': 'Thursday',
    'viernes': 'Friday',
    'sabado': 'Saturday',
    'domingo': 'Sunday'}   
    fechas = pd.to_datetime(df['release_date'], format= '%Y-%m-%d')
    n_dia = fechas[fechas.dt.strftime('%A').str.capitalize() == day_translated[str(dia).lower()]]
    respuesta = n_dia.shape[0]
    return {'mes':dia, 'cantidad':respuesta}

@app.get('/franquicia/{franquicia}')
def franquicia(franquicia):
    f_low=franquicia.lower()
    fran=df[['belongs_to_collection','revenue']].dropna(subset=['belongs_to_collection'])
    fran=fran[fran['belongs_to_collection'].map(str.lower).apply(lambda x: f_low in x)]
    cantidad=fran.shape[0]
    ganancia_total=fran['revenue'].sum()
    ganancia_promedio=fran['revenue'].mean()
    return {'franquicia':franquicia, 'cantidad':cantidad, 'ganancia_total':ganancia_total, 'ganancia_promedio':ganancia_promedio}

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais):
    m1 = df[['title', 'production_countries']]
    if isinstance(pais, str):
        pais = pais.lower()
        pais = unicodedata.normalize('NFKD', pais).encode('ascii', 'ignore').decode('utf-8','ignore')
        cantidad = m1['title'][m1['production_countries'].str.contains(pais)==True]
        cantidad = df['production_countries'].apply(lambda x: str(x).lower()).map(str.lower).apply(lambda x: pais in x)
        respuesta = cantidad.shape[0]
    return {'pais': pais, 'cantidad': respuesta}

@app.get('/productoras/{productora}')
def productoras(productora):
    prod=df[['production_companies','revenue']].dropna()
    prod['production_companies']=prod['production_companies'].map(str.lower)
    prod=prod[prod.production_companies.str.contains(productora.lower(), regex=False)]
    cantidad=prod.sum()
    ganancia_total=prod['revenue'].sum()
    return {'productora':productora, 'ganancia_total':ganancia_total, 'cantidad':cantidad}

@app.get('/retorno/{pelicula}')
def retorno(pelicula):
    pelicula_df = df.loc[df['title'] == pelicula.title()]
    inversion = pelicula_df['budget'].iloc[0].item()
    ganancia = pelicula_df['revenue'].iloc[0].item()
    retorno= pelicula_df['return'].iloc[0].item()
    anio = pelicula_df['release_year'].iloc[0].item()
    return {'pelicula': pelicula, 'inversion': inversion, 'ganancia': ganancia, 'retorno': retorno, 'anio': anio}

@app.get('/recomendacion/{titulo}')
def recomendacion(titulo):
    idx = indices[titulo]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key= lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    recommendations=list(ml['title'].iloc[movie_indices].str.title())
    return {'lista recomendada': recommendations}

