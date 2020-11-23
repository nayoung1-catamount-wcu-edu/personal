#include <iostream>
using std::cout;
using std::cin;

#include <string>
using std::string;

#include <vector>
using std::vector;
using std::begin;
using std::end;

#include <algorithm>
using std::sort;
using std::count;

int main()
{
	vector<int> nums;

	for (int i = 0; i < 10; i++)
	{
		nums.push_back(i);
	}

	for (auto item : nums)
	{
		cout << item << " ";
	}
	cout << '\n';

	vector<string> words;

	cout << "Enter three words:\n";
	for (int i = 0; i < 3; i++)
	{
		string s;
		cin >> s;
		words.push_back(s);
	}

	for (auto item : words)
	{
		cout << item << " ";
	}
	cout << '\n';

	cout << "int vector nums has " << nums.size() << " elements." << '\n';

	nums[5] = 3;
	nums[6] = -1;
	nums[1] = 99;

	for (auto item : nums)
	{
		cout << item << " ";
	}
	cout << '\n';

	for (unsigned int i = 0; i < nums.size(); i++)
	{
		cout << nums[i] << " ";
	}
	cout << '\n';

	for (auto i = begin(nums); i != end(nums); i++)
	{
		cout << *i << " ";
	}
	cout << '\n';

	sort(begin(words), end(words));
	for (auto item : words)
	{
		cout << item << " ";
	}
	cout << '\n';

	int threes = count(begin(nums), end(nums), 3);
	cout << "Vector of ints has " << threes << " elements with value 3" << '\n';

	int tees = count(begin(words[0]), end(words[0]), 't');
	cout << "First word has " << tees << " letter t's" << '\n';

	return 0;
}