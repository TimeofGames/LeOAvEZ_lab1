#include <iostream>
#include <random>
#include <time.h>

int main()
{
    srand(time(NULL));
    int lenght;
    scanf_s("%d", &lenght);
    int* massive = (int*)malloc(lenght*sizeof(int));
    for (int i = 0;i < lenght;i++) {
        massive[i] = rand() % 200 - 100;
    }
    for (int i = 0;i < lenght;i++) {
        printf("%4d ", massive[i]);
    }
}

