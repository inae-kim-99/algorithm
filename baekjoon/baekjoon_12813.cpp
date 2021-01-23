#include<iostream>
#include <string>
#define SIZE 100000
using namespace std;
int A[SIZE], B[SIZE];
string a_str, b_str;

int main() {

	cin >> a_str >> b_str;
	for (int i = 0; i < SIZE; i++) {
		A[i] = a_str[i] - '0';
		B[i] = b_str[i] - '0';
	}

	// A&B
	for (int i = 0; i < SIZE; i++)
		cout << (A[i] & B[i]);
	cout << "\n";

	// A|B
	for (int i = 0; i < SIZE; i++)
		cout << (A[i] | B[i]);
	cout << "\n";

	// A^B
	for (int i = 0; i < SIZE; i++)
		cout << (A[i] ^ B[i]);
	cout << "\n";

	// ~A
	for (int i = 0; i < SIZE; i++)
		cout << (!A[i]);
	cout << "\n";

	// ~B
	for (int i = 0; i < SIZE; i++)
		cout << (!B[i]);
	cout << "\n";

	return 0;
}