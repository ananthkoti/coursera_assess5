#include <iostream>
using namespace std;
  struct s1{
        char rno[4];
        char name[10];
        char phno[4];
        char mks[4];
        char attendance[10];
    };
    struct s1 s2[4];
int main()
{
    int i;
    for(i=0;i<=3;i++)
    {
  cout<<"\nEnter student rollno:";
  cin>>s2[i].rno;
  cout<<"\nEnter Name:";
  cin>>s2[i].name;
  cout<<"\nEnter phone number";
  cin>>s2[i].phno;
  cout<<"\nEnter marks:";
  cin>>s2[i].mks;
  cout<<"Enter attendance:";
  cin>>s2[i].attendance;
    }
    for(i=0;i<=3;i++)
    {
  cout<<"\n"<<s2[i].rno;
  cout<<"\n"<<s2[i].name;
  cout<<"\n"<<s2[i].phno;
  cout<<"\n"<<s2[i].mks;
  cout<<"\n"<<s2[i].attendance;
    }
    return 0;

}