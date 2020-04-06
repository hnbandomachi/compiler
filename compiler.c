#include<stdio.h>
#include<stdlib.h>
int main() {
int x;
int y;
int z;
int a;
int b;
int c;
int d;
printf("Enter x = "); scanf("%d", &x);
printf("Enter y = "); scanf("%d", &y);
printf("Enter z = "); scanf("%d", &z);
a = x + y;
b = y - z;
c = x * z;
d = a / b;
printf("Result a = %d ", a );
printf("Result b = %d ", b );
printf("Result c = %d ", c );
printf("Result d = %d ", d );
system("pause");
return 0;
}