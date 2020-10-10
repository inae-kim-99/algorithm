#include <iostream>
#include<string>
#include<vector>
using namespace std;
int answer[2002][2002]; // ��

int main() {

	int N,M; // ������ ũ��, ������ ����
	cin >> N;

	int numbers[2002];  // ĥ�ǿ� ���� ��
	for (int i = 0; i < N; i++)
		cin >> numbers[i];
	cin >> M;

	for (int dif=0; dif < N; dif++) { // dif : ���̰�
		for (int a = 0;a+dif < N; a++) { // b : ���۰�
			int b = a + dif;
			//�� �ϳ� - �Ӹ����
			if (dif == 0) {
				answer[a][b] = 1;
				continue;
			}
			else if (dif == 1) { // �� �ΰ�
				if (numbers[a] == numbers[b]) // ������ �Ӹ����
					answer[a][b] = 1;
				else
					answer[a][b] = 0;
				continue;
			}
			else if (numbers[a] == numbers[b] && answer[a + 1][b - 1] == 1) { // �� ���� ���� �� ������ ������ �Ӹ������ ��
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