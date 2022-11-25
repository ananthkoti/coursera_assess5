#include <iostream>
using namespace std;
int main() {
    int i,N,count=0;
    cout<<"enter the change to be returned ";
    cin>>N;
    int arr[10]={1,2,5,10,20,50,100,500,1000,2000};
    for(i=9;i>=0;i--){
        while(N>=arr[i]){
            N=N-arr[i];
             cout<<" "<<N<<endl;
            count++;
        }
        }
    cout<<count;
    return 0;
}