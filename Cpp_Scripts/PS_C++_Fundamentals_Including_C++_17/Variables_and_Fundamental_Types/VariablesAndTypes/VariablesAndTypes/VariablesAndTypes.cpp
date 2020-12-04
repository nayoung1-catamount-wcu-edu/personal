#include <iostream>

int main()
{
	// Initializing with an equals sign
	int i1 = 1;
	std::cout << "il = " << i1 << std::endl;

	// Split as two lines with i2 is uninitialized in line 10
	int i2;
	i2 = 2;
	std::cout << "i2 = " << i2 << std::endl;

	// Initialization with parentheis
	int i3(3);
	std::cout << "i3 = " << i3 << std::endl;

	// Initialization with braces
	int i4{ 4 };
	std::cout << "i4 = " << i4 << std::endl;


	double d1 = 2.2;
	double d2 = i1;
	//int i5 = d1;
	int i5 = static_cast<int>(d1);
	std::cout << "d1 = " << d1 << std::endl;
	std::cout << "d2 = " << d2 << std::endl;
	std::cout << "i5 = " << i5 << std::endl;


	char c1 = 'a';
	//char c2 = "b";
	std::cout << "c1 = " << c1 << std::endl;
	//std::cout << "c2 = " << c2 << std::endl;

	bool flag = false;
	std::cout << "flag = " << flag << std::endl;
	
	flag = i1;
	std::cout << "flag = " << flag << std::endl;

	flag = d1;
	std::cout << "flag = " << flag << std::endl;


	auto a1 = 1;
	auto a2 = 2.2;
	auto a3 = 'c';
	auto a4 = "s";
	auto a5 = true;
	auto a6 = 3L;
	auto a7 = 1'000'000'000'000;
	auto a8 = 0xFF;
	auto a9 = 0b111;

	//a1 = a2;
	a1 = static_cast<int>(a2);

	return 0;	 
}