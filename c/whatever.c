#include <stdio.h>
#include <stdbool.h>
#include "five.h"

void main(){
    int x = 5;
    int *y = &x;

    printf("x: %d &x: %d *x: can't! y: %d *y: %d &y: %d", x, &x, y, *y, &y);
    //printf("%d%d", 5, 5);

    printf("\n");
}

