#include <iostream>
using std::cout;
using std::cin;

#include <string>
using std::string;

int main()
{
	// declare dtypes of variables
	string phrase1;
	string phrase2;


	// get value for word 1
	//cout << "Enter a word: ";
	//cin >> word1;

	// get value for phrase 1
	cout << "Enter a phrase: ";
	getline(cin, phrase1);

	// get value for word 2
	//cout << "Enter another word: ";
	//cin >> word2;

	// get value for phrase 2
	cout << "Enter another phrase: ";
	getline(cin, phrase2);

	// check length of variables
	if (phrase1.length() == phrase2.length()) {
		cout << "\nBoth inputs are the same length.";
	}

	if (phrase1.length() > phrase2.length()) {
		cout << "\nThe first input is longer than the second input.";
	}

	if (phrase1.length() < phrase2.length()) {
		cout << "\nThe second input is longer than the first input.";
	}
	return 0;
}