#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"Enter a number";
    cin>>n;
    int i=1;
    int sum=0;
    while(i<=n){
        cout<< "Current value of i is: "<<i<<"\n";
        sum=sum+i;
        i++;
    }
    cout<<"The total of entered numbe is: "<< sum;        
    
    return 0;

}

