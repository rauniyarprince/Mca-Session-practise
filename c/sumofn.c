#include<stdio.h>
int main(){
  int n,sum=0,num;
  printf("enter the count num which you want to add:");
  scanf("%d",&n);
  for(int i=1;i<=n;i++){
    printf("enter the number %d");
    scanf("%d",&num);
    sum +=num;
  }
  printf("total num : %d",sum);
  return 0;
}