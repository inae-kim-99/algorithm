#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

int main() {

	int N, M;
	cin >> N >> M;

	vector<vector<int>> connect;
	vector<int> v;
	connect.assign(N+1, v);
	vector<int> link;
	link.assign(N + 1, 0);
	queue<int> q;

	// 연결 정보 입력
	while (M--) {
		int A, B;
		cin >> A >> B;
		connect[A].push_back(B);
		link[B]++;
	}
	// 앞 순서가 없는 학생 push
	for (int i = 1; i <= N; i++)
		if (!link[i])
			q.push(i);

	while(!q.empty()) {
		int front = q.front();
		q.pop();
		for (int i = 0; i < connect[front].size(); i++) {
			int B = connect[front][i];
			if ((--link[B]) == 0) {
				q.push(B);
			}
		}
		cout << front << " ";
	}
	return 0;
}