#include <iostream>
#include "head.h"

template<class T>
void minimum(T no1, T no2)
{
    if (no1 < no2)
    {
        std::cout << no1 << std::endl;
    }
    else
    {
        std::cout << no2 << std::endl;
    }
}
template <>
void minimum<std::string>(std::string no1, std::string no2)
{
    int znak1 = no1.size();
    int znak2 = no2.size();
    if (znak1 < znak2)
    {
        std::cout << no1 << std::endl;
    }
    else
    {
        std::cout << no2 << std::endl;
    }
}