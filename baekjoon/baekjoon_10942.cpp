#include <iostream>
#include<string>
#include<vector>
using namespace std;
int answer[2002][2002]; // 답

int main() {

	int N,M; // 수열의 크기, 질문의 개수
	cin >> N;

	int numbers[2002];  // 칠판에 적은 수
	for (int i = 0; i < N; i++)
		cin >> numbers[i];
	cin >> M;

	for (int dif=0; dif < N; dif++) { // dif : 차이값
		for (int a = 0;a+dif < N; a++) { // b : 시작값
			int b = a + dif;
			//수 하나 - 팰린드롬
			if (dif == 0) {
				answer[a][b] = 1;
				continue;
			}
			else if (dif == 1) { // 수 두개
				if (numbers[a] == numbers[b]) // 같으면 팰린드롬
					answer[a][b] = 1;
				else
					answer[a][b] = 0;
				continue;
			}
			else if (numbers[a] == numbers[b] && answer[a + 1][b - 1] == 1) { // 두 수가 같고 그 사이의 수열이 팰린드롬일 때
				answer[a][b] = 1;
				continue;
			}
			else
				answer[a][b] = 0;
		}
	}

	for (int i = 0; i < M; i++) {
		int S, E;
		cin >> S >> E;
		cout << answer[S - 1][E - 1] << endl;
	}

	return 0;
}