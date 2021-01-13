// https://www.acmicpc.net/problem/15922

#include <iostream>
using namespace std;
int main() {

	int N;
	cin >> N;

	int end = -1000000000, total_length = 0;
	while (N--) {
		int x, y;
		cin >> x >> y; // 선분 x, y 값 입력
		if (x < end) { // x가 이전 y의 최대값 보다 작다면
			if (y < end) // y가 이전 y의 최대값 보다 작다면 PASS (이미 포함)
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