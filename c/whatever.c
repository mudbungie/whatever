#include <stdio.h>
#include <stdbool.h>
//#include <random.h>
#include <stdlib.h>
#include "five.h"


struct thing {
    int x;
};

struct thing gimme_a_thing(int attribute_value) {
    struct thing the_thing;
    the_thing.x = attribute_value;
    return the_thing;
}

void main(){
    struct thing the_thing = gimme_a_thing(2);

    struct thing *thing_address;
    thing_address = &the_thing;

    printf("%d", the_thing.x);
    printf("%d", thing_address->x);

    // for (int i = 0; i < 5; i++){
    //     //printf("%d", thing.x);
    //     printf("%d", thing);
    // }

    printf("\n");
}

