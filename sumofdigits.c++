#include<iostream>
using namespace std;
int main()
{
    int n;
    int last_digits;
    int sum=0;
    int i;
    cout<<"Enter a number: ";
    cin>>n;
    for(i=0;i<=n;i++){
        last_digits=n%10;
        sum=sum+last_digits;
        n/=10;
    }
    cout<<"The Sum of the Digits are:"<<sum;
}
