#include<iostream>
using namespace std;
int main(){
    int rows,cols,i=0;
    cout<<"Enter the number of rows"<<endl;
    cin>>rows;
    cout<<"Enter the number of cols"<<endl;
    cin>> cols;
    // while(i<=rows){
    //     int j=1;
    //     while(j<=cols){
    //         cout<<"*"<<" ";
    //         j++;
    //     }
    //     cout<<endl;
    //     i++;
    // }
    while(i<rows){
        int j=0;
        while(j<cols){
            cout<<i<<"";
            j++;
        }
        cout<<endl;
        i++;
    }
    return 0;
}