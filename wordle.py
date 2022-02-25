import typer
import json
from datetime import datetime, timezone



# Constante, long de cada palabra
LONG_PALABRA = 5

# Creo objeto typer para linea de comando
app = typer.Typer()

def color_letra(letra, color):    
    if color == 'amarillo':
        return (f"\x1b[0;37;43m{letra}\x1b[0m")
    elif color == 'verde':
        return (f"\33[42m{letra}\x1b[0m")
    else:
        return (f"\33[105m{letra}\x1b[0m")

def obtenar_palabra_dia():
    
    dia_hoy = datetime.today().strftime('%Y%m%d')

    with open("palabras_por_fecha.json", "r", encoding='utf-8') as j:
        palabras_por_fecha = json.load(j)

    return palabras_por_fecha[dia_hoy]

def imprimir_teclado(palabras_usuario, palabra_wordle):
    # Crear teclado
    cadena_teclado = list("[ Q ][ W ][ E ][ R ][ T ][ Y ][ U ][ I ][ O ][ P ]\n[ A ][ S ][ D ][ F ][ G ][ H ][ J ][ K ][ L ][ Ñ ]\n       [ Z ][ X ][ C ][ V ][ B ][ N ][ M ]")

    bandera_letra = 0
    # palabras_usuario1 = palabra_usuario
    
    for palabra_usuario in palabras_usuario:
        x = 0
        ubicacion_letra = 0
        bandera_letra = 0
        
        while x < LONG_PALABRA:
            # Itero cadena_teclado
            for tecla in cadena_teclado:
                # Llevo cuenta de la ubicacion
                ubicacion_letra += 1
                # si encuentro letra
                if palabra_usuario[x].upper() == tecla:
                    # si letra no tiene caracteres al costado suyo, realizo busqueda de caracteres a llenar
                    if cadena_teclado[ubicacion_letra - 2] == ' ':
                        if (palabra_usuario[x] in palabra_wordle):
                            if palabra_wordle[x] == palabra_usuario[x]:
                                simbolos = "=="
                                # palabra_usuario[x] = color_letra(palabra_usuario[x], "verde")
                                # cadena_teclado[ubicacion_letra - 1] = color_letra(cadena_teclado[ubicacion_letra - 1], "verde")
                            else:
                                simbolos = "><"
                                # palabra_usuario[x] = color_letra(palabra_usuario[x], "amarillo")
                                # cadena_teclado[ubicacion_letra - 1] = color_letra(cadena_teclado[ubicacion_letra - 1], "amarillo")
                        else:
                            simbolos = "<>"
                            # palabra_usuario[x] = color_letra(palabra_usuario[x], "gris")
                            # cadena_teclado[ubicacion_letra - 1] = color_letra(cadena_teclado[ubicacion_letra - 1], "gris")

                        # Lleno teclado con <>, == o ><
                        cadena_teclado[ubicacion_letra - 2] = simbolos[0]
                        cadena_teclado[ubicacion_letra] = simbolos[1]
                    # si simbolo de letra es '='
                    elif cadena_teclado[ubicacion_letra - 2] == '=':
                        # rompo iteracion sobre teclado pues no es necesario hacer nada 
                        break
                    # si se debe cambiar simbolo de letra
                    elif cadena_teclado[ubicacion_letra - 2] == '>':
                        if palabra_usuario[x] == palabra_wordle[x]:
                            cadena_teclado[ubicacion_letra - 2] = '='
                            cadena_teclado[ubicacion_letra] = '='
                            # palabra_usuario[x] = color_letra(palabra_usuario[x], "verde")  
                            # cadena_teclado[ubicacion_letra - 1] = color_letra(cadena_teclado[ubicacion_letra - 1], "verde")                      

            # Aumento cuenta de posicion de caracter de letra        
            x += 1
            # Reinicio ubicacion de letra pues estoy buscando una nueva
            ubicacion_letra = 0            

    for tecla in cadena_teclado:
        print(tecla, end='')
    print("")

palabra1 = ''

def resumen_partida(palabras_usuario, palabra_wordle):
    unicode_caracter_gris = "\u2B1C"
    unicode_caracter_amarillo = "\U0001F7E8"
    unicode_caracter_verde = "\U0001F7E9"

    dic_caracteres = {
        'gris': unicode_caracter_gris,
        'amarillo': unicode_caracter_amarillo, 
        'verde': unicode_caracter_verde
    }

    for palabra_usuario in palabras_usuario:
        x = 0
        while x < LONG_PALABRA:
            if palabra_usuario[x] in palabra_wordle:
                if palabra_wordle[x] == palabra_usuario[x]:
                    print(dic_caracteres['verde'],end='')
                else:
                    print(dic_caracteres['amarillo'],end='')
            else:
                print(dic_caracteres['gris'],end='')          

            # Aumento cuenta de posicion de caracter de letra        
            x += 1
            if x == 5:
                print('')

def imprimir_letras_intentos(palabras_usuario, palabra_wordle):
    
    # imprimir_caracteres_if()
    cadena_inicial = "+---+---+---+---+---+\n|   |   |   |   |   |\n+---+---+---+---+---+\n|   |   |   |   |   |\n+---+---+---+---+---+\n|   |   |   |   |   |\n+---+---+---+---+---+\n|   |   |   |   |   |\n+---+---+---+---+---+\n|   |   |   |   |   |\n+---+---+---+---+---+\n|   |   |   |   |   |\n+---+---+---+---+---+\n"
    # Transformar cadena inicial en una lista compuesta por cada elemento de la cadena
    cadena_inicial = list(cadena_inicial)

    # Diccionario con la pos inicial de la grafica de cada intento, facilita ingreso de letras
    intentos_dic = {
        1: 22,
        2: 66,
        3: 110,
        4: 154,
        5: 198,
        6: 242
    }

    # Inicializo variables
    intentos = 0
    ganar_juego = 0

    # Itero sobre lista de palabras ingresadas por usuario
    for palabra_usuario in palabras_usuario:
        # Variable intentos variará dependiendo de la cantidad de palabras en palabras_usuario
        intentos += 1
        # inicializar x para iterar sobre la palabra a llenar
        x = 0
        cuenta = 0
        while x < LONG_PALABRA:

            # Asignar cada caracter de la palabra en cadena inicial
            cadena_inicial[intentos_dic[intentos] + (x * 4 + 2)] = palabra_usuario[x]

            if palabra_usuario[x] in palabra_wordle:
                cadena_inicial[intentos_dic[intentos] + (x * 4 + 2) - 1] = ">"
                cadena_inicial[intentos_dic[intentos] + (x * 4 + 2) + 1] = "<"
                
            else:
                cadena_inicial[intentos_dic[intentos] + (x * 4 + 2) - 1] = "<"
                cadena_inicial[intentos_dic[intentos] + (x * 4 + 2) + 1] = ">"
                
            if palabra_wordle[x] == palabra_usuario[x]:
                cadena_inicial[intentos_dic[intentos] + (x * 4 + 2) - 1] = "="
                cadena_inicial[intentos_dic[intentos] + (x * 4 + 2) + 1] = "="
            x += 1                

        # Verifico en fila de la palabra si se cumplió con los requerimientos para ganar
        for caracter in cadena_inicial[intentos_dic[intentos]:(intentos_dic[intentos] + (x * 4 + 2) + 1) - 2]:
            if caracter == '=':
                cuenta +=1
                if cuenta == 10:
                    ganar_juego = 1

        
    # Imprimir lista final
    for caracter in cadena_inicial:
        print(caracter, end='')
    print('')

    if ganar_juego:
        return True



def guardar_partidas(palabras_usuario):    

    # Hora en formato RFC 3339
    hora_local = datetime.now(timezone.utc).astimezone().isoformat()
    palabras_partida = []
    # Diccionario para json 
    diccionario_partida = {}
    # Lista vacia para json
    lista_partidas = []

    # Transformo cada palabra (list) en str para mejor visualizacion en json file
    for palabra in palabras_usuario:
        palabra = ''.join(palabra)
        palabras_partida.append(palabra)

    # Json diccionario listo, key es la hora local y su value la lsita de cada palabra de la partida
    diccionario_partida[hora_local] = palabras_partida

    # Si archivo json ya tiene contenido
    try:
        with open("partidas.json", "r+", encoding='utf-8') as j:
            # cargo contenido de json file        
            partidas_json = json.load(j)
            # añado nuevo diccionario de partida finalizada
            partidas_json.append(diccionario_partida)
            # cambio posicion de archivo json a 0        
            j.seek(0)
            # traspaso nuevo diccionario a json file
            json.dump(partidas_json, j)
    # En caso de que archivo json esté vacío
    except:
        with open("partidas.json", "a", encoding='utf-8') as j:
            lista_partidas.append(diccionario_partida)
            json.dump(lista_partidas, j)    

@app.command()
def obtener_confirmacion_input(confirmacion: str):
    abecedario = "abcdefghijklmnñopqrstuvwxyzü"
    vocales_tilde = {'á': 'a',
                'é': 'e',
                'í': 'i',
                'ó': 'o',
                'ú': 'u'}

    confirmacion = confirmacion.lower().strip()

    if confirmacion == 'y' or confirmacion == 'yes':
        
        # Inicializo cantidad de intentos
        intentos = 0

        # Inicializo variable
        palabras_usuario = []

        # Siempre pide intento de palabra
        while True:
            # Input de usuario
            palabra_usuario = input("Ingresar palabra: ").lower().strip()
            # Transformo str a lista para mejor manejo
            palabra_usuario = list(palabra_usuario)    

            # Si longitud de palabra no es 5 continúo con siguiente iteración
            if len(palabra_usuario) != LONG_PALABRA:
                print("Ingresa palabra de 5 caracteres")
                continue

            # Flag para detectar input correcto, asumo que siempre será correcto
            input_correcto = 1

            # Primera letra de palabra ingresada
            i = 0
            while i < len(palabra_usuario):
                # Si caracter de palabra no es letra de abecedario y no es vocal con tilde
                if (palabra_usuario[i] not in abecedario) and (palabra_usuario[i] not in vocales_tilde.keys()):
                    print("Ingresar caracteres del idioma español")
                    # Flag a 0, input incorrecto
                    input_correcto = 0
                    break

                # Si caracter de palabra es vocal con tilde, se cambia a vocal sin tilde
                if palabra_usuario[i] in vocales_tilde.keys():
                    palabra_usuario[i] = vocales_tilde[palabra_usuario[i]]   
                # Siguiente caracter de palabra ingresada
                i += 1
        
            # Obtengo palanra de hoy
            palabra_wordle_hoy = obtenar_palabra_dia()

            # Si input es correcto, palabra se manda a funcion para imprimir resultado
            if input_correcto:
                # Creo lista de palabras, lista crecerá a medida de que no se gane y de que palabra ingresada por usuario sea correcta
                palabras_usuario.append(palabra_usuario)
                # 6 intentos
                if intentos < 6:
                    # Aumento intentos
                    intentos += 1       
                    resultado = imprimir_letras_intentos(palabras_usuario, palabra_wordle_hoy)
                    imprimir_teclado(palabras_usuario, palabra_wordle_hoy)
                    if resultado:
                        print("\nGanaste el juego\n")
                        resumen_partida(palabras_usuario, palabra_wordle_hoy)
                        guardar_partidas(palabras_usuario)
                        break
                    if intentos == 6:
                        print("\nPerdiste\n")
                        resumen_partida(palabras_usuario, palabra_wordle_hoy)
                        guardar_partidas(palabras_usuario)
                        break

if __name__ == '__main__':
    # obtener_confirmacion_input("yes") # para debugging
    app()