#include <iostream>
using namespace std;

int min(int a, int b) {
	return a > b ? b : a;
}

int main() {

	int k2, k3, k5, k6;
	cin >> k2 >> k3 >> k5 >> k6;

	int make_256 = min(k2, min(k5, k6)); // k2, k5, k6 중에 가장 적은 개수로 256 만들기
	int make_32 = k2 > make_256 ? min(k3, k2 - make_256) : 0; // 256 제외하고 숫자 2가 남았다면

	cout << make_256 * 256 + make_32 * 32;

	return 0;
}