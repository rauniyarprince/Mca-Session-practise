#include<stdio.h>
int main(){
  int num1,num2;
  printf("enter the first num: ");
  scanf("%d",&num1);
   printf("enter the Second num: ");
  scanf("%d",&num2);
  float result =(float) num1/num2;
  printf("Result: %f",result);
  return 0;
}