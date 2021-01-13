// https://www.acmicpc.net/problem/15922

#include <iostream>
using namespace std;
int main() {

	int N;
	cin >> N;

	int end = -1000000000, total_length = 0;
	while (N--) {
		int x, y;
		cin >> x >> y; // ���� x, y �� �Է�
		if (x < end) { // x�� ���� y�� �ִ밪 ���� �۴ٸ�
			if (y < end) // y�� ���� y�� �ִ밪 ���� �۴ٸ� PASS (�̹� ����)
				continue;
			else
				total_length += (y - end);
		}
		else
			total_length += (y - x);

		end = y;
	}

	cout << total_length;

	return 0;
}