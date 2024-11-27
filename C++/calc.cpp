#include<iostream>
using namespace std;
int main(){
    int a,b;
    char c;
    cout<<"Enter First Number"<<endl;
    cin>>a;
    cout<<"Enter Second Number"<<endl;
    cin>>b;
    cout<<"Enter the Operation"<<endl;
    cin>>c;
    //cout<<a<<b<<c;
    switch(c){
    case '+': cout<<a+b<<endl;
    break;
    case '-': cout<<a-b<<endl;
    break;
    case '*': cout<<a*b<<endl;
    break;
    case '/': cout<<a/b<<endl;
    break;
    default: cout<<"Enter valid operation";
    }
}