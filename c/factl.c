#include<stdio.h>
int square(int a){
  return a*a;
}
int main(){
  int num;
   printf("Enter the num:");
   scanf("%d",&num);
   printf(square(num));
   return 0 ;
   
}