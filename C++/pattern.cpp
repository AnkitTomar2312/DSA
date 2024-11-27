#include<iostream>
using namespace std;
int main(){
    int rows,cols,i=1;
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
    // while(i<rows){
    //     int j=0;
    //     while(j<cols){
    //         cout<<i<<"";
    //         j++;
    //     }
    //     cout<<endl;
    //     i++;
    // }
    /*
    1234
    1234
    1234
    1234
    */
//    while(i<=rows){
//     int j=1;
//     while(j<=cols){
//         cout<<j<<" ";
//         j++;
//     }
//     cout<<endl;
//     i++;
//    }
/*
4321
4321
4321
4321
 */
// while(i<=rows){
//     int j=cols;
//     while(j>=1){
//         cout<<j<<" ";
//         j--;
//     }
//     cout<<endl;
//     i++;
// }
/*
123
456
789
*/
int count=1;
while(i<=rows){
    int j=1;
    while(j<=cols){
        cout<<count<<" ";
        count++;j++;
    }
    cout<<endl;
    i++;

}
    return 0;
}