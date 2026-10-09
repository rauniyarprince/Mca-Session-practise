#include<stdio.h>
void swap(int a,int b){
  int temp;
  temp = a;
  a = b;
  b = temp;
  printf("a = %d, b=%d",a,b);
}
int main(){
  int x = 10; 
  int y = 20;
   swap(x,y);
  printf("x=%d, y=%d",x,y);
 

}