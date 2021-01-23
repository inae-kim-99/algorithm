#include <iostream>
#include <string>
#include <cstring>
#include <math.h>
using namespace std;
int words[25]; // ��Ʈ����ũ�� ǥ���� �ܾ��
int full, canTest, N, answer; // full : ��� �ܾ� ������ ���, canTest : ��� ���ĺ� ������ ���, N : �ܾ� ����, answer : ����

void dfs(int idx, int alphabets) {
	// ���� ������ �ܾ��� �׽�Ʈ�� ������ ���
	if (alphabets == canTest) {
		answer += pow(2, N - idx); // ������ ����� �� ��� ���
		return;
	}
	// ��� Ȯ���� ���
	if (idx == N)
		return;

	// ���
	dfs(idx + 1, alphabets);
	dfs(idx + 1, alphabets | words[idx]);
}

int main() {

	cin >> N;

	memset(words, 0, sizeof(int) * 25);

	for (int i = 0; i < N; i++) {
		string word;
		cin >> word;
		for (int j = 0; j < word.length(); j++) { // �ܾ ��Ʈ����ũ�� ǥ��
			words[i] |= (1 << (word[j] - 'a'));
		}
	}

	full = (1 << N) - 1;
	canTest = (1 << 26) - 1;

	dfs(0, 0);

	cout << answer << endl;

	return 0;
}