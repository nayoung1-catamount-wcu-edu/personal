// While.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using std::cout;
using std::cin;
using std::endl;

int main()
{
    int x;
    cout << "Enter a number" << endl;
    cin >> x;

    bool prime = true;
    int i;
    for (i = 2; i <= x / i; i = i + 1)
    {
        int factor = x / i;
        if (factor * i == x)
        {
            cout << "factor found: " << i << " * " << factor << endl;
            prime = false;
            break;
        }
    }

    cout << i << endl;


    cout << x << " is ";
    if (prime)
        cout << "prime" << endl;
    else
        cout << "not prime" << endl;

    return 0;
}
