"Imagina que esta API es una biblioteca de películas.. la función load_movies() es como un bibliotecario que carga el catalogo de libros (película) cuando se abre la biblioteca. La función get_movies() muestra todo el catalogo cuando alguien lo pide. La función get_movie(id) es como si alguien preguntara por una película específica por su codigo de identificación. La función chatbot (query) es un asistente que busca películas según palabras claves y sinonimo. La función get_movies_by_category(category) ayuda a encontrar películas según su genero(acciob, comedia, etc)"

# importamos las erramienantas para construir nuestra api
from fastapi import FastAPI, HTTPException #fast api nos ayuda a crear la API, HTTPexeption maneja errores

from fastapi.responses import HTMLResponse, JSONResponse # HTMLResonse para paginas web, JSONResponse para respuestas en formato JSON

import pandas as pd #pandas nos ayuda a manejar datos en tablas como si fuera un excel
import nltk #nltk es una libreria par procesar texto y analizar palabras
from nltk.tokenize import word_tokenize #se usa para dividir un texto en palabras individuales
from nltk.corpus import wordnet #nos ayuda a encontrar sinonimos de palabras.
