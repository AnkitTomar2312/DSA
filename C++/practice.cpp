#include<iostream>
using namespace std;
int main(){
    // int a=9;
    // if(a==9){
    //     cout<<"NINEY";
    // }
    // if(a>0){
    //     cout<<"POSITIVE";
    // }
    // else{
    //     cout<<"NEGATIVE";
    // }
    // cout<<"\n";
    // int n=24;
    // if(n>20){
    //     cout<<"Love";
    // }
    // else if(n==24){
    //     cout<<"Lovely";
    // }
    // else{
    //     cout<<"Babbar";
    // }
    // cout<<n;
// int i=10,j=1;
// while(j<i){
// char c;
// cout<<"Enter a number"<<endl;
// cin>>c;
// int  num=int(c);
// if(num>96 && num<123){
//     cout<<c<<" is a Lower Alphabet";
// }
// else if(num>64 && num<91){
//     cout<<c<<" is a Capital Alphabet";
// }
// else if(num>47 && num<58){
//  cout<<c<<" is a Number";   
// }
// cout<<endl;
// j++;
// }
int n=10,a=0,b=1;
cout<<a<<" "<<b<<" ";
for(int i=0;i<=n;i++){
    int nextN=a+b;
    cout<<nextN<<" ";
    a=b;
    b=nextN;
}
return 0;
}

