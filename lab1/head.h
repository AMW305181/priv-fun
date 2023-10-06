#pragma once
#include <string>
#include <iostream>
constexpr int maxWiersz = 10;
constexpr int maxKolumna = 10;
template <class T>
void minimum(T no1, T no2);

template <class T>
class Macierz
{
    int wiersz;
    int kolumna;
    T macierz[maxWiersz][maxKolumna];
    public:
    Macierz (int w, int k)
    {
        this->wiersz = w;
        this->kolumna = k;

    };
    void ustElement (int nr_wiersza, int nr_kolum, T wartosc)
    {
        this->macierz[nr_wiersza][nr_kolum]=wartosc;
    };
    void wyswietlMacierz() 
    {
        for (int i = 0; i < this->wiersz; i++)
        {
            for (int j = 0; j < this->kolumna; j++)
            {
                std::cout << macierz[i][j] << " ";
            }
            std::cout << std::endl;
        }
    };
    Macierz odejTablice(Macierz mac1, Macierz mac2)//zakladajac, ze macierze maja ten sam rozmiar
    {
        Macierz nowa_macierz(mac1->wiersz, mac1->kolumna);
        for(int i=0; i<mac1->wiersz; i++)
        {
            for(int j=0; j<mac1->kolumna;j++)
            {
                nowa_macierz.ustElement(i, j, mac1[i][j]-mac2[i][j]);
            }
        }
        return nowa_macierz;
    };
};

template <class T>
class Macierz_2 : Macierz<T>
{
    public:
    Macierz_2(int w, int k)
    {
        
        this->wiersz = w;
        this->kolumna = k;
    }
    Macierz_2 dod_Macierze(Macierz_2<T> mac1, Macierz_2<T> mac2)
    {
        Macierz_2 nowa_macierz=Macierz_2(mac1->wiersz, mac1->kolumna);
        for(int i=0; i<mac1->wiersz; i++)
        {
            for (int j=0; j<mac1->kolumna; j++)
            {
                nowa_macierz.ustElement(i,j,mac1[i][j]+mac2[i][j]);
            }
        }
        return nowa_macierz;
    }
};