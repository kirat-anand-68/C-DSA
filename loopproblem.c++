#include<iostream>
using namespace std;
int main(){
    
    int n;
    int i;
    int j;
    cout<<"Enter the number of lines: ";
    cin>>n;
    for(i=1;i<=2*n-1;i++){
        for(j=1;j<=2*n-1;j++){
            int a=i;
            int b=j;
            if(a>n) a=2*n-i;
            if(b>n)  b=2*n-j;
            int x=min(a,b);
            cout<<n-x+1;
        }
        cout<<endl;
    }
}
