#include<iostream>
using namespace std;
void sub(int x)
{
    int i=0;
    int arr[i];

    while(x!=0)
    {
        arr[i] = x%10;
        x = x/10;
        arr[i]>arr[i+1];
        i++;
    }
    
}
int main()
{
    
    int num;
    cout<<"Enter a nuumber \n";
    cin>>num;
    sub(num);
    return 0;
}

