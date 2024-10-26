#include<iostream>
using namespace std;

int BinSrch(int arr[],int key,int size){
    int start=0;
    int end=size-1;
    int mid=start+(end-start)/2;
    while(start<=end){
        if(arr[mid]==key){
            return mid;
        }
        else if (arr[mid]<key){
            start=mid+1;
        }
        else{
            end=mid-1;
        }
        mid=start+(end-start)/2;
    }
    return -1;
}

int main(){

int odd[5]={4,7,18,40,58};
int even[6]={4,7,18,40,58,70};
int oddser=BinSrch(odd,58,5);
cout<<"This is the odd arr result: "<<oddser<<endl;
int evenser=BinSrch(even,40,6);
cout<<"This is the even arr result: "<<evenser<<endl;
}