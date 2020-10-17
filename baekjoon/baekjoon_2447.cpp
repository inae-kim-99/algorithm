#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<vector<bool>> square;

void star(int n, int row, int col) { // 재귀 함수
	int size = n / 3;
	if (n != 1) {
		for (int i = 0; i < 3; i++) { // 9개의 공간으로 나누어 각각 재귀 함수 실행. 가운데 제외
			for (int j = 0; j < 3; j++) {
				if (!(i == 1 && j == 1)) {
					star(size, i * size+row, j * size+col);
				}
			}
		}
		for (int i = size; i < size * 2; i++) // 가운데 false로 채우기
			for (int j = size; j < size * 2; j++)
				square[row + i][col + j] = false;
	}
}

int main() {

	int N;
	cin >> N;

	vector<bool> v;
	v.assign(N, true);
	square.assign(N, v);
	
	star(N/3, 0, 0);
	
	// CODE 1
	//for (int i = 0; i < N; i++) {
	//	for (int j = 0; j < N; j++)
	//		cout << (square[i][j] ? "*" : " ");
	//	cout << "\n";
	//}

	// CODE 2
	for (int i = 0; i < 3; i++) {
		if (i != 1) {
			for (int a = 0; a < N / 3; a++) {
				for (int r = 0; r < 3; r++) {
					for (int b = 0; b < N / 3; b++) {
						cout << (square[a][b] ? "*" : " ");
					}
				}
				cout << "\n";
			}
		}
		else {
			for (int a = 0; a < N / 3; a++) {
				for (int r = 0; r < 3; r++) {
					if (r != 1) {
						for (int b = 0; b < N / 3; b++) {
							cout << (square[a][b] ? "*" : " ");
						}
					}
					else {
						for (int b = 0; b < N / 3; b++) {
							cout << " ";
						}
					}
					
				}
				cout << "\n";
			}
		}
	}

	return 0;
}



