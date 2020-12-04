// If.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using std::cout;
using std::cin;
using std::endl;

int main()
{
    int x, y;
    cout << "Enter two numbers" << endl;
    cin >> x >> y;

    cout << x << " ";
    if (x > y)
    {
        cout << "is larget than ";
    }
    else
    {
        cout << "is not larger than ";
    }
    cout << y << endl;

    if (x + y > 10)
    {
        cout << "thanks for choosing larger numbers!" << endl;
    }

    return 0;
}