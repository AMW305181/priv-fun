export module matematyka:podstawowe_operacje;
export import <vector>;

export int dodawanie(std::vector<int> liczby)
{
	int wynik = 0;
	for (int i = 0; i < liczby.size(); i++)
	{
		wynik += liczby[i];
	}
	return wynik;
};

export int odejmowanie(int pierwsza, int druga)
{
	return pierwsza -= druga;
}