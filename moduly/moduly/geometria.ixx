export module geometria;
import <cmath>;

export class Kwadrat
{
	int bok;
public:
	Kwadrat(int b) : bok(b) {};
	int pole()
	{
		return bok * bok;
	}
	double przekatna()
	{
		return bok * sqrt(2);
	}
	int obwod()
	{
		return bok * 4;
	}
};

export class Trojkat;

class Trojkat
{
	int bok;
public:
	Trojkat(int b) : bok(b) {};
	double pole()
	{
		return (bok * bok * sqrt(3)) / 4;
	};
	int obwod()
	{
		return bok * 3;
	};
};

export double kolo_pole(int promien);
export double kolo_obwod(int promien);