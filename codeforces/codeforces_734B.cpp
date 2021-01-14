#include <iostream>
using namespace std;

int min(int a, int b) {
	return a > b ? b : a;
}

int main() {

	int k2, k3, k5, k6;
	cin >> k2 >> k3 >> k5 >> k6;

	int make_256 = min(k2, min(k5, k6)); // k2, k5, k6 �߿� ���� ���� ������ 256 �����
	int make_32 = k2 > make_256 ? min(k3, k2 - make_256) : 0; // 256 �����ϰ� ���� 2�� ���Ҵٸ�

	cout << make_256 * 256 + make_32 * 32;

	return 0;
}