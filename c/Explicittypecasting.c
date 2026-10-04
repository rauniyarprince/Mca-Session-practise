#include<stdio.h>
int main(){
  float num;
  printf("Enter the floating num: ");
  scanf("%f",&num);
  int result = (int)num;
  printf("Explicit converstion: %d",result);
  return 0;
}