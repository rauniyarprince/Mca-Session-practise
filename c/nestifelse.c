#include<stdio.h>
int main(){
  int num ;
  printf("enter the number :");
  scanf("%d",&num);
  if(num<0)
  printf("negative num");
  else if(num>0)
  printf("postive num");
  else if(num == 0)
  printf("given num is zero");
  else
  printf("invalid");
  return 0;
}