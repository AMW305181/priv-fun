export module matematyka:zaawansowane_operacje;
import <iostream>;

export int mnozenie(int pierwsza, int druga)
{
	return pierwsza * druga;
};

export int dzielenie(int pierwsza, int druga)
{
	if (druga == 0)
	{
		std::cout << "Nie dzielimy przez 0";
		return 0;
	}
	else
	{
		return pierwsza / druga;
	}
}
