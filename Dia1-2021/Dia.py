profundidad = []
suma_total = 0

with open('valores.txt', 'r') as archivo:
    contendo_archivo = archivo.readlines()
    
    for line in contendo_archivo:
        profundidad.append(line.strip())
# print(profundidad)

for i in range(0, (len(profundidad) - 1)):
    print(f"elemento1: {profundidad[i+1]}, elemento2: {profundidad[i]}")
    if profundidad[i+1] > profundidad[i]:
        suma_total += 1
print(suma_total)