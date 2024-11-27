#include <iostream>
using namespace std;

int counter(int a)
{
    int counter = 0;
    while (a != 0)
    {
        int dig = a % 10;
        if (dig == 1)
        {
            counter++;
        }
        a/=10;
    }
    cout<<"counter loop "<< counter<<endl;
    
}

int decToBin(int n)
{
    string toBin = "";
    while (n != 0)
    {
        int bit = n & 1;
        toBin = to_string(bit) + toBin;
        n = n >> 1;
    }
    int binary=stoi(toBin);
    cout<<"decToBin Loop"<<binary<<endl;
    counter(binary);

}



int main()
{
    int a, b;
    cin >> a>>b;
    decToBin(a);
    decToBin(b);
    
}
// I am not able to save it continue....