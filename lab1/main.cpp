
#include <iostream>
#include<string>
#include "head.h"

int main()
{
    minimum(2, 3);
    std::string s1 = "bubu";
    std::string s2 = "mairabu";
    minimum(s1, s2);
    Macierz<int> mac1(8, 8);
    for(int i=0;i<8;i++)
    {
        for(int j=0; j<8; j++)
        {
            mac1.ustElement(i,j,10);
        }
    }
    mac1.wyswietlMacierz();
    return 0;
}