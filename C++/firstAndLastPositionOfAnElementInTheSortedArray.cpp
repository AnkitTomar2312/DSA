//First and last position of an element in the sorted array

#include<iostream>
using namespace std;
//First we will find the first Occurence:-
int firstOccu(int arr[],int size,int k){
//Approach of first Occurence function agr element mil gya h to first occurence ko find krne ke liye hm end-1 krenge.
int start=0;
int end=size-1;
int mid=start+(end-start)/2;
int loc=-1;
while(start<=end){
    if(arr[mid]==k){
        loc=mid;
        mid=end-1;
    }
    else if(arr[mid]<k){
        start=mid+1;
    }
    else{
        end=mid-1;
    }
    mid=start+(end-start)/2;
}



}
int main(){


}