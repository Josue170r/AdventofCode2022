lista_mochilas = []

with open("valores.txt", 'r') as archivo:
    contenido = archivo.readlines()

    for line in contenido:
        lista_mochilas.append(line.strip())
# print(lista_mochilas)

suma_prioridad = 0
lista_minusculas = [chr(letra) for letra in range(ord('a'), ord('z') + 1)]
lista_mayusculas = [chr(letra) for letra in range(ord('A'), ord('Z') + 1)]

diccionario_letras = {}

for indice, letra in enumerate(lista_minusculas, start=1):
    diccionario_letras[letra] = indice

for indice, letra in enumerate(lista_mayusculas, start=27):
    diccionario_letras[letra] = indice

# Imprimir el diccionario
# print(diccionario_letras)

suma_insignea = 0
elfosporGrupo1 = []
elfosporGrupo2 = []
elfosporGrupo3 = []

for _, mochila in enumerate(lista_mochilas[::3]):
    elfosporGrupo1.append(mochila)

for _, mochila in enumerate(lista_mochilas[1::3]):
    elfosporGrupo2.append(mochila)

for _, mochila in enumerate(lista_mochilas[2::3]):
    elfosporGrupo3.append(mochila)

for index, mochila in enumerate(elfosporGrupo1):
    contador_elementos = 0
    for insignea in mochila:
        if (insignea in elfosporGrupo2[index] and insignea in elfosporGrupo3[index] and contador_elementos == 0):
            contador_elementos += 1
            suma_insignea += diccionario_letras[insignea]
    
print(suma_insignea)