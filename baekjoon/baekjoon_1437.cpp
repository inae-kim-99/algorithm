#include <iostream>
#include <cstring>
#define ll long long
using namespace std;

int main() {

	int N;
	cin >> N;

	long long answer = 1;
	while (N >= 5) {
		answer *= 3;
		N -= 3;
	}
	answer *= N;

	cout << answer % 10007;

	return 0;
}
