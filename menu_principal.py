
LONG_PALABRA = 5


def imprimir_caracteres_if():
    caracteres_inicio_final = '+---'
    print(caracteres_inicio_final*5, end='')
    print('+')

def imprimir_letras_intentos(palabra_usuario, intentos, palabra_wordle):
    
    imprimir_caracteres_if()
    cadena_inicial = "|   |   |   |   |   |"
    # Transformar cadena inicial en una lista compuesta por cada elemento de la cadena
    cadena_inicial = list(cadena_inicial)


    # inicializar x para iterar sobre la palabra a llenar
    x = 0    
    while x < LONG_PALABRA:

        # Asignar cada caracter de la palabra en cadena inicial
        cadena_inicial[4 * x + 2] = palabra_usuario[x]

        if palabra_usuario[x] in palabra_wordle:
            cadena_inicial[4 * x + 1] = ">"
            cadena_inicial[4 * x + 3] = "<"
        else:
            cadena_inicial[4 * x + 1] = "<"
            cadena_inicial[4 * x + 3] = ">"
        if palabra_wordle[x] == palabra_usuario[x]:
            cadena_inicial[4 * x + 1] = "="
            cadena_inicial[4 * x + 3] = "="
             

        x += 1

    ganar_juego = 0
    cuenta = 0
    # Imprimir lista final
    for caracter in cadena_inicial:
        if caracter == '=':
            cuenta +=1
            if cuenta == 10:
                ganar_juego = 1
        print(caracter, end='')
    print('')

    if ganar_juego:
        # print("\nGanaste el juego")
        return True

abecedario = "abcdefghijklmnñopqrstuvwxyz"
vocales_tilde = {'á': 'a',
                'é': 'e',
                'í': 'i',
                'ó': 'o',
                'ú': 'u'}

# Inicializo cantidad de intentos
intentos = 0

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

    # Si input es correcto, palabra se manda a funcion para imprimir resultado
    if input_correcto:        
        # 6 intentos
        if intentos < 6:
            # Aumento intentos
            intentos += 1       
            resultado = imprimir_letras_intentos(palabra_usuario, intentos, "cacas")
            if resultado:
                print("\nGanaste el juego")
                break
            if intentos == 6:
                break