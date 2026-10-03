#include <stdio.h>

int main() {
    int i = 0;
    int fact = 1;

    while (i <= 1) {
        fact = fact * (i == 0 ? 1 : i);

        printf("Factorial of %d = %d\n", i, fact);

        i++;
    }

    return 0;
}