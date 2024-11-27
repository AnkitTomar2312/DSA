#include <iostream>
using namespace std;
int main()
{
    int amt;
    cout << "Enter the Amount" << endl;
    cin >> amt;
    // 100,50,10,1 eg=1330
    int hund=0, fifty=0, ten=0, one=0;
    while (amt != 0)
    {
        if (amt >= 100)
        {
            hund = amt / 100;
            amt = amt - (hund * 100);
           
        }
    
        else if (amt >= 50)
        {
            fifty = amt / 50;
            amt = amt - (fifty * 50);
          
        }
        
        else if (amt >= 10)
        {
            ten = amt / 10;
            amt = amt - (ten * 10);
            
        }
        
        else
        {
            one = amt / 1;
            amt = amt - (one * 1);
            
        }
    }
    cout<<"You Need "<<hund<<" 100 rupee notes, "<<fifty<<" fifty rupee notes, "<<ten<<" ten rupee notes, "<<one<<" one rupee notes";
    
}
