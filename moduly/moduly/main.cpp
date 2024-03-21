import pozdrowienia;
import statystyka;
import geometria;


int main()
{
	std::cout << "Poprawne rozwiazanie zadania 1:" << std::endl;
	czesc_misiu_pysiu();
	std::cout << oczka_juz_sie_kleja() << std::endl;
	std::cout << "*********************************" << std::endl;

	std::cout << "Poprawne rozwiazanie zadania 2:" << std::endl;
	std::cout << "Test funkcji modulu matematyka:" << std::endl;
	std::vector<int> rzeczy{ 2,6,89,97 };
	std::cout << "Test dodawania na vectorze {2,6,89,97}: " << dodawanie(rzeczy) << std::endl;
	std::cout << "Test odejmowania na liczbach 5 i 8: " << odejmowanie(5,8) << std::endl;
	std::cout << "Test mnozenia na liczbach 4 i 9: " << mnozenie(4, 9) << std::endl;
	std::cout << "Test dzielenia na liczbach 6 i 3: " << dzielenie(6, 3) << std::endl;
	std::cout << "Test dzielenia na liczbach 1 i 0: " << dzielenie(1, 0) << std::endl;
	std::cout<<"Test sredniej na vectorze {2,6,89,97}: "<< srednia(rzeczy) << std::endl;
	std::cout << "*********************************" << std::endl;

	std::cout << "Poprawne rozwiazanie zadania 3:" << std::endl;
	Kwadrat kwadrat = Kwadrat(4);
	std::cout << "Test pole kwadratu o boku 4: " << kwadrat.pole() << std::endl;
	std::cout << "Test przekatna kwadratu o boku 4: " << kwadrat.przekatna() << std::endl;
	std::cout << "Test obwod kwadratu o boku 4: " << kwadrat.obwod() << std::endl;
	Trojkat trojkat = Trojkat(3);
	std::cout << "Test pole trojkata rownobocznego o boku 3: " << trojkat.pole() << std::endl;
	std::cout << "Test obwod trojkata rownobocznego o boku 3: " << trojkat.obwod() << std::endl;
	std::cout << "Test pole kola o promieniu 5: " << kolo_pole(5) << std::endl;
	std::cout << "Test obwod kola o promieniu 5: " << kolo_obwod(5) << std::endl;
	return 0;
}
