// ClassesAndObjects.cpp : Defines the entry point for the console application.
//

#include "Person.h"
#include "Tweeter.h"
#include "Status.h"
#include <iostream>
using std::cout;
using std::endl;
using std::string;

int main()
{
	Person p1("Nate", "Young", 123);
	{
		Tweeter t1("Someone", "Else", 456, "@whoever");
		std::string name2 = t1.GetName();
	}
	cout << "after innermost block" << endl;
	cout << "p1: " << p1.GetName() << " " << p1.GetNumber() << endl;
	p1.SetNumber(124);
	cout << "p1: " << p1.GetName() << " " << p1.GetNumber() << endl;

	return 0;
}
	