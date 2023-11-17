cadena = "lvcNpRHDCnTLCJlL"

# Inicializamos un diccionario para contar la frecuencia de cada letra
frecuencia_letras = {}

# Iteramos sobre las letras de la cadena
for letra in cadena:
    frecuencia_letras[letra] = frecuencia_letras.get(letra, 0) + 1

# Buscamos las letras que se repiten más de una vez
letras_repetidas = [letra for letra, frecuencia in frecuencia_letras.items() if frecuencia > 1]

# Imprimimos el resultado
if letras_repetidas:
    print(f"Las letras que se repiten son: {', '.join(letras_repetidas)}")
else:
    print("No hay letras que se repitan más de una vez.")