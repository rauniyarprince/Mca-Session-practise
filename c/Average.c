#include <stdio.h>
int main() {
    int n, list, sum = 0;

    printf("Enter the number of values: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        printf("Enter number %d: ", i);
        scanf("%d", &list);
        sum = sum + list;
    }

    float result = (float)sum / n;

    printf("Average of numbers: %f\n", result);

    return 0;
}