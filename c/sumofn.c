// #include<stdio.h>
// int main(){
//   int n,sum=0,num;
//   printf("enter the count num which you want to add:");
//   scanf("%d",&n);
//   for(int i=1;i<=n;i++){
//     printf("enter the number:");
//     scanf("%d",& num);
//     sum +=num;
//   }
//   printf("total num %d :",sum);
//   return 0;
// }

#include <stdio.h>

int main() {
int i = 1, sum = 0, num, n;

```
printf("Enter the count of numbers: ");
scanf("%d", &n);

while (i <= n) {
    printf("Enter the number: ");
    scanf("%d", &num);

    sum += num;
    i++;
}

printf("Total sum: %d\n", sum);

return 0;
```

}
