#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"Enter a number ";
    cin>>n;
    int i=0;
    int sum=0;
    // while(i<=n){
    //     cout<< "Current value of i is: "<<i<<"\n";
    //     sum=sum+i;
    //     i++;
    // }
    // cout<<"The total of entered numbe is: "<< sum;      
    while(i<=n){
        if(i%2==0){
            cout<<i<<"-is a Prime Number"<<endl;
            sum=sum+i;
        }
        i++;
    }
    cout<<"The sum of the entered even nmbers are: "<<sum;
    return 0;

}

