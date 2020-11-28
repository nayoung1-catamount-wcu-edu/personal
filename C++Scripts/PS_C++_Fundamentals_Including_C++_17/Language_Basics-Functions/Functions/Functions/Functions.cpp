// Functions.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using std::cout;
using std::cin;
using std::endl;

#include "Utility.h"

int main()
{
	int x;
	cout << "Enter a number" << endl;
	cin >> x;

	if (IsPrime(x))
		cout << x << " is prime" << endl;
	else
		cout << x << " is not prime" << endl;

	if (Is2MorePrime(x))
		cout << x << "+2 is prime" << endl;
	else
		cout << x << "+2 is not prime" << endl;

	return 0;
}
