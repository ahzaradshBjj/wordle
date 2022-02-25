# contador = 0
# with open('palabras.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()

file = open("palabras.txt", "r", encoding='utf-8')
file2 = open('palabras5.txt', 'w', encoding='utf-8')

vocales_tilde = {'á': 'a',
                'é': 'e',
                'í': 'i',
                'ó': 'o',
                'ú': 'u'}


# x es cada palabra de lista-general
for x in file:
    # Si palabra de listado tiene 5 caracteres (6 incluyendo salto de línea)
    if len(x) == 6:
        # transformo x a lista para una mejor manipulación
        x = list(x)

        # Variable para iterar sobre palabra
        i = 0
        while i < 5:
            # Si pos i de palabra de 5 caracteres es una letra con tilde, la intercambiamos por la misma vocal sin tilde
            if x[i] in vocales_tilde.keys():
                x[i] = vocales_tilde[x[i]]   
            i += 1

        # Transforo palbra a str nuevamente ya que write acepta solo este tipo de dato
        x = ''.join(x)
        # Escribo palabra en file2
        file2.write(x)

file.close()
file2.close()


    