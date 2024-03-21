export module statystyka;
export import matematyka;

export double srednia(std::vector<int> liczby)
{
	return dzielenie(dodawanie(liczby), liczby.size());
};