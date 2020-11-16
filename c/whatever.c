#include <stdio.h>
#include <stdbool.h>

void main(){
    bool desired_truthiness = true;

    int thing = 4;
    bool truthy = false;
    if ( ! desired_truthiness ){
        printf("yes");
        int truthy = 1;
    }
    else {
        printf("no");
        int truthy = 2;
    }

    //printf("%d", thing);
    //printf("%d", 4 == thing);
    printf("%d", truthy);
    printf("\n");
}