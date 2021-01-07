#include <iostream>
#include <cstring>
#define ll long long
using namespace std;

ll memo[1000001];

ll check(int num) {

	if (num == 1 || num == 2 || num == 3 || num == 4) // 1,2,3,4 -> 곱의 최대값은 자기 자신
		return memo[num] = num;
	else if (memo[num] != -1) // 이전에 계산한 값이 있다면 return
		return memo[num];

	ll max = 0;
	for (int a = 1; a <= num / 2; a++) {
		ll mul = check(a) * check(num - a);
		if (mul > max)
			max = mul;
	}

	if (num > max)
		max = num;

	return (memo[num] = max);
}

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