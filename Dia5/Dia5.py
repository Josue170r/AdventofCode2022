with open("input_test.txt") as f:
    lines = f.read().splitlines()
    print(lines)

for i, linea in enumerate(lines):
    if linea == "":
        indice_elemento_vacio = i
print(indice_elemento_vacio)        