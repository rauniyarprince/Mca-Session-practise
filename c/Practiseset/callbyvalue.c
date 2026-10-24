#include<stdio.h>
void pass(int a,int b){
int temp;
temp = a;
a = b;
b = temp;
printf("from function: a= %d , b=%d\n",a,b);
}
int main(){
  int m;
  printf("enter the number:");
  scanf("%d",&m);
  printf("enter num:%d\n",m);
  int n;
  printf("enter the number: \n");
  scanf("%d",&n);
  printf("enter num:%d\n",n);
  pass(m,n);
  printf("form main value: a=%d , b=%d",m,n);
  return 0; 
  
}
