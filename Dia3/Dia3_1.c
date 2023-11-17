#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // Declaración e inicialización de variables
    char lista_mochilas[100][100];  // Puedes ajustar el tamaño según tus necesidades
    int suma_prioridad = 0;
    char lista_minusculas[26];
    char lista_mayusculas[26];
    char diccionario_letras[52];
    int tam_compartimiento;

    // Llenar listas de letras
    for (int i = 0; i < 26; ++i) {
        lista_minusculas[i] = 'a' + i;
        lista_mayusculas[i] = 'A' + i;
    }

    // Llenar diccionario de letras
    for (int i = 0; i < 26; ++i) {
        diccionario_letras[i] = lista_minusculas[i];
        diccionario_letras[i + 26] = lista_mayusculas[i];
    }

    // Abrir archivo y leer mochilas
    FILE *archivo = fopen("valores.txt", "r");
    if (archivo == NULL) {
        perror("Error al abrir el archivo");
        return 1;
    }

    int mochilas_count = 0;
    char linea[100];

    while (fgets(linea, sizeof(linea), archivo) != NULL) {
        strcpy(lista_mochilas[mochilas_count], linea);
        lista_mochilas[mochilas_count][strlen(lista_mochilas[mochilas_count]) - 1] = '\0';  // Eliminar el carácter de nueva línea
        mochilas_count++;
    }

    fclose(archivo);

    // Procesar mochilas
    for (int k = 0; k < mochilas_count; ++k) {
        tam_compartimiento = strlen(lista_mochilas[k]) / 2;
        char *cadena_actual = lista_mochilas[k];
        char compartimiento1[50];
        char compartimiento2[50];

        // Llenar compartimiento1
        for (int i = 0; i < tam_compartimiento; ++i) {
            compartimiento1[i] = cadena_actual[i];
        }
        compartimiento1[tam_compartimiento] = '\0';

        // Llenar compartimiento2
        for (int i = tam_compartimiento, j = 0; i < strlen(cadena_actual); ++i, ++j) {
            compartimiento2[j] = cadena_actual[i];
        }
        compartimiento2[strlen(cadena_actual) - tam_compartimiento] = '\0';

        int contador_elementos = 0;

        // Comparar compartimientos y calcular suma de prioridad
        for (int i = 0; i < tam_compartimiento; ++i) {
            for (int j = 0; j < strlen(compartimiento2); ++j) {
                if (compartimiento1[i] == compartimiento2[j] && contador_elementos == 0) {
                    suma_prioridad += i + j + 1;
                    contador_elementos += 1;
                }
            }
        }
    }

    printf("La suma total es: %d\n", suma_prioridad);

    return 0;
}
