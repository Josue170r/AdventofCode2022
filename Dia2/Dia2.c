#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_ROWS 2500

int main() {
    char movimientos_elfo[MAX_ROWS];
    char lista_movimientos[MAX_ROWS];
    int suma_ronda = 0;
    int sumatotal = 0;
    FILE *fp;

    fp = fopen("valores.txt", "r+t");

    if (fp == NULL) {
        fp = fopen("valores.txt", "w+t");
    } else {
        int row = 0;

        while (fscanf(fp, " %c %c", &movimientos_elfo[row], &lista_movimientos[row]) == 2 && row < MAX_ROWS) {
            ++row;
        }
    }

    fflush(fp);
    fclose(fp);

    // printf("Movimientos Elfo: ");
    // for (int i = 0; i < MAX_ROWS; i++) {
    //     printf("%c ", movimientos_elfo[i]);
    // }
    // printf("\n");

    // printf("Lista Movimientos: ");
    // for (int i = 0; i < MAX_ROWS; i++) {
    //     printf("%c ", lista_movimientos[i]);
    // }
    // printf("\n");

    //! Parte 1 del probrama
    // for(int i = 0; i <2500; i++) {
    //   switch(movimientos_elfo[i]){
    //     case 'A':
    //       if (lista_movimientos[i] == 'X'){
    //         suma_ronda += 4;
    //       } else if (lista_movimientos[i] == 'Y') {
    //         suma_ronda += 8;
    //       } else {
    //         suma_ronda += 3;
    //       }
    //       sumatotal += suma_ronda;
    //       suma_ronda = 0;
    //     break;
    //     case 'B':
    //       if(lista_movimientos[i] == 'X'){
    //         suma_ronda += 1;
    //       } else if (lista_movimientos[i] == 'Y') {
    //         suma_ronda += 5;
    //       } else {
    //         suma_ronda += 9;
    //       }
    //       sumatotal += suma_ronda;
    //       suma_ronda = 0;
    //     break;
    //     default: 
    //       if (lista_movimientos[i] == 'X') {
    //         suma_ronda += 7;
    //       } else if (lista_movimientos[i] == 'Y') {
    //         suma_ronda += 2;
    //       } else {
    //         suma_ronda += 6;
    //       }
    //       sumatotal += suma_ronda;
    //       suma_ronda = 0;
    //     break;
    //   }
    // }

    //!Parte 2 del problema
    for(int i = 0; i <2500; i++) {
      switch(movimientos_elfo[i]){
        //Case 1 = Piebra
        case 'A':
          if (lista_movimientos[i] == 'X'){
            suma_ronda += 3;
          } else if (lista_movimientos[i] == 'Y') {
            suma_ronda += 4;
          } else {
            suma_ronda += 8;
          }
          sumatotal += suma_ronda;
          suma_ronda = 0;
        break;
        //Case 2 = Papel
        case 'B':
          if(lista_movimientos[i] == 'X'){
            suma_ronda += 1;
          } else if (lista_movimientos[i] == 'Y') {
            suma_ronda += 5;
          } else {
            suma_ronda += 9;
          }
          sumatotal += suma_ronda;
          suma_ronda = 0;
        break;
        //Case 3 = Tijeras
        default: 
          if (lista_movimientos[i] == 'X') {
            suma_ronda += 2;
          } else if (lista_movimientos[i] == 'Y') {
            suma_ronda += 6;
          } else {
            suma_ronda += 7;
          }
          sumatotal += suma_ronda;
          suma_ronda = 0;
        break;
      }
    }
    printf("%d\n", sumatotal);

    return 0;
}
