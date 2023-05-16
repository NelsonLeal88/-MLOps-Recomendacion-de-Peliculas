**PROYECTO INDIVIDUAL - MACHINE LEARNING**

CASO A SOLUCIONAR

Una start-up que provee servicios de agregación de plataformas de streaming, desea mejorar su propuesta de valor, para ello nos acaba de contratar para desarrollar un sistema de recomendacion con Machine Learning.
Se llevaron a cabo las diferentes sesiones para poder entrenar al modelo y asi poder resolver las consultas de prediccion. La data no estaba totalmente limpia, por lo que habia que arreglarla y dejar los archivos listos para la fase de creacion de la API, hacer el EDA y finalmente entrenar el modelo.

TRABAJO A REALIZAR

- Transformación y limpieza de datos
- Desarrollo de API
- Análisis exploratorio de datos (EDA).
- Modelo de Machine learning

DESARROLLO DE LAS API`S

- peliculas_mes(mes):
Esta función recibe el mes y devuelve la cantidad de películas que se estrenaron en ese mes
- peliculas_dia(dia):
Esta función recibe el día de la semana y devuelve la cantidad de películas que se estrenaron en ese día
- franquicia(franquicia):
Esta función recibe el nombre de una franquicia y devuelve la cantidad de películas de esa franquicia, su ganancia total y promedio
- peliculas_pais(pais):
Esta función recibe el nombre de un país y devuelve la cantidad de películas en ese paísre del país
- productoras(productora):
Esta función recibe el nombre de una productora y devuelve la ganancia total y la cantidad de películas que a producido
- retorno(pelicula):
Esta función recibe el nombre de una película y devuelve la inversion, ganancia, retorno y año de lanzamiento de la película

DEPLOYMENT
Para esta fase se propuso usar RENDER

EDA - ANALISIS EXPLORATORIO DE DATOS

Codigo Consulta API Aqui dejamos el codigo de las consultas desarrolladas y probadas:

https://github.com/NelsonLeal88/Proyecto1/blob/main/EDA.ipynb

SISTEMA DE RECOMENDACION - MODELO MACHINE LEARNING
Una vez realizado y verificado el EDA se entrena el modelo de machine learning para armar el sistema de recomendacion de peliculas para el usuario

Codigo modelo machine learning - sistema de recomendacion Aqui dejamos el codigo del modelo entrenado de machine learning:

https://github.com/NelsonLeal88/Proyecto1/blob/main/ML.ipynb
