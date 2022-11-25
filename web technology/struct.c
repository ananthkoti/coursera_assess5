#include<stdio.h>
int main(){
    struct s1{
        char name[20];
        int age;
        float sal;
    };
    struct emp e={"tiger"}
    printf("%d%d%f",e.age,e.sal);
}