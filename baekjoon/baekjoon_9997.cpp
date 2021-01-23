#include <iostream>
#include <string>
#include <cstring>
#include <math.h>
using namespace std;
int words[25]; // 비트마스크로 표현한 단어들
int full, canTest, N, answer; // full : 모든 단어 포함한 경우, canTest : 모든 알파벳 포함한 경우, N : 단어 개수, answer : 정답

void dfs(int idx, int alphabets) {
	// 현재 선택한 단어들로 테스트가 가능한 경우
	if (alphabets == canTest) {
		answer += pow(2, N - idx); // 나머지 경우의 수 모두 계산
		return;
	}
	// 모두 확인한 경우
	if (idx == N)
		return;

	// 재귀
	dfs(idx + 1, alphabets);
	dfs(idx + 1, alphabets | words[idx]);
}

int main() {

	cin >> N;

	memset(words, 0, sizeof(int) * 25);

	for (int i = 0; i < N; i++) {
		string word;
		cin >> word;
		for (int j = 0; j < word.length(); j++) { // 단어를 비트마스크로 표현
			words[i] |= (1 << (word[j] - 'a'));
		}
	}

	full = (1 << N) - 1;
	canTest = (1 << 26) - 1;

	dfs(0, 0);

	cout << answer << endl;

	return 0;
}