#include <iostream>
using std::cout;
using std::cin;

#include <string>
using std::string;

int main()
{
	string name;
	cout << "Who are you? ";
	cin >> name;
	string greeting = "Hello, " + name;
	if (name == "Nate")
	{
		greeting += ", I know you!";
	}
	cout << greeting << '\n';

	int l = greeting.length();
	cout << "\"" + greeting + "\" is " << l << " characters long." << '\n';
	string beginning = greeting.substr(greeting.find(' ') + 1);
	cout << beginning << '\n';
	if (beginning == name)
	{
		cout << "expected result." << '\n';
	}


	return 0;
}