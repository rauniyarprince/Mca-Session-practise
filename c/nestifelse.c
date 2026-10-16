#include<stdio.h>
int main(){
  int num ;
  printf("enter the number :");
  scnaf("%d",&num);
  if(num<0)
  printf("negative num");
  elseif(num>0)
  printf("postive num");
  elseif(num == 0)
  printf("given num is zero");
  else
  printf("invalid")




}