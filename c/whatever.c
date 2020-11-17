#include <stdio.h>
#include <stdbool.h>
#include "five.h"

void main(){
    printf("does this print?\n");
    int five = gimme_five();
    printf("this is five: %d", five);
    printf("\n");

    char a_string[] = "hey, strings are a thing, can they contain %d\n";
    printf(a_string, 3);

    printf("\n");
}

