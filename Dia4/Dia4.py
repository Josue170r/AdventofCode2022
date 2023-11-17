asignacion_Elfo1 =[]
asignacion_Elfo2 = []
pareja_elfos = []
suma_total = 0

with open("valores.txt", 'r') as archivo:
    contenido = archivo.readlines()

    for line in contenido:
        pareja_elfos.append(line.strip())

for elfo in pareja_elfos:
    elfo1, elfo2 = elfo.split(',')
    asignacion_Elfo1.append(elfo1)
    asignacion_Elfo2.append(elfo2)

#! Parte 1 del día 4
for elfo1, elfo2 in zip(asignacion_Elfo1, asignacion_Elfo2):
    inicio, fin = map(int, elfo1.split('-'))
    conjunto_A = set(range(inicio,fin+1))
    inicio, fin = map(int, elfo2.split('-'))
    conjunto_B = set(range(inicio,fin+1))
    if(conjunto_B.issubset(conjunto_A) or conjunto_A.issubset(conjunto_B)):
        suma_total += 1
print(suma_total)
suma_total = 0

#! Parte 2 del día 4
for elfo1, elfo2 in zip(asignacion_Elfo1, asignacion_Elfo2):
    inicio, fin = map(int, elfo1.split('-'))
    conjunto_A = set(range(inicio,fin+1))
    inicio, fin = map(int, elfo2.split('-'))
    conjunto_B = set(range(inicio,fin+1))
    intersection = conjunto_A.intersection(conjunto_B)
    if(intersection):
        suma_total += 1
print(suma_total)