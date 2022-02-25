from dateutil import  rrule
from datetime import datetime

a = '20220101'
b = '20221231'

# Lista de fechas del 2022, formado YYYYMMDD
lista_fechas = []

# Fechas de año 2022
for dt in rrule.rrule(rrule.DAILY, dtstart=datetime.strptime(a, '%Y%m%d'), until=datetime.strptime(b, '%Y%m%d')):
    # agrego fecha de cada día del año a lista_fechas
    lista_fechas.append(dt.strftime('%Y%m%d'))

# Abrir palabras5.txt
file = open('palabras5.txt', 'r', encoding='utf-8')

# Lista para almacenar todas las palabras del archivo
palabras = []

# Iterar sobre cada palabra de archivo
for x in file:
    # transformar str a lista
    x = list(x)
    # Elimino caracter de salto de linea de txt
    x.pop()
    # Transformo lista a str
    x = ''.join(x)
    # Agrego palabra a la lista de palabras
    palabras.append(x)

file.close()

# Generar 365 palabras
import random

# Con sample nos aseguramos que no haya repeticion de palabras
palabras_365 = random.sample(palabras, 365)

# Creo diccionario para almacenar bdd de fecha y palabra
diccionario_bdd = {}

# 365 fechas y palabras
for i in range(0, 365):
    # Obtengo cada fecha de lista_fechas, comenzando con el primer dia del año
    fecha = lista_fechas[i]
    # Agrego al diccionario el key fecha, cuyo valor será la primer palabra al azar de la lista palabras_365
    diccionario_bdd[fecha] = palabras_365[i]

# print(diccionario_bdd)
# Crear archivo palabras_por_fecha.json
import json

with open("palabras_por_fecha.json", "w", encoding='utf-8') as j:
    # Paso diccionario_bdd al archivo json
    json.dump(diccionario_bdd, j)




