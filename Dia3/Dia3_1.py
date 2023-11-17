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
print(diccionario_letras)

for mochila in lista_mochilas:
    tam_compartimiento = int(len(mochila) / 2)
    cadena_actual = mochila
    compartimiento1 = []
    compartimiento2 = []
    for indice, item in enumerate(cadena_actual[:tam_compartimiento]):
        compartimiento1.append(item)
        
    for (indice, item) in enumerate(cadena_actual[tam_compartimiento:len(cadena_actual)]): 
        compartimiento2.append(item)

    contador_elementos = 0
    for valor_compartimiento in compartimiento1:
        if (valor_compartimiento in compartimiento2) and (contador_elementos == 0):
            print(valor_compartimiento)
            suma_prioridad += diccionario_letras[valor_compartimiento]
            contador_elementos += 1

print(f"La suma total es: {suma_prioridad}")