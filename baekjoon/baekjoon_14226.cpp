#include <iostream>
#include<string>
#include<vector>
#include<queue>
using namespace std;

int visited[1001][1001]; // 화면, 클립보드

int main() {
	ios_base::sync_with_stdio(false);
	int S;
	cin >> S;
	queue<pair<int, int>> q;
	q.push(make_pair(1, 0));
	visited[1][0] = 0;
	int min = -1;

	while (!q.empty()) {
		int screen = q.front().first;
		int clip = q.front().second;
		q.pop();

		if (visited[screen][screen] == 0) {
			visited[screen][screen] = visited[screen][clip] + 1; // 복사
			q.push(make_pair(screen, screen));
		}
		if (screen + clip <= S && visited[screen + clip][clip] == 0) {
			visited[screen + clip][clip] = visited[screen][clip] + 1;
			q.push(make_pair(screen + clip, clip));
		}
		if (screen - 1 >= 0 && visited[screen - 1][clip] == 0) {
			visited[screen - 1][clip] = visited[screen][clip] + 1;
			q.push(make_pair(screen - 1, clip));
		}
	}
	for (int i = 0; i <= S; i++) {
		if (visited[S][i] != 0) {
			if (min == -1 || min > visited[S][i]) {
				min = visited[S][i];
			}
		}
	}
	cout << min;

	return 0;
}