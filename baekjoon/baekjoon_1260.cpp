// https://www.acmicpc.net/problem/1260
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
vector<int> node[1001];
bool check[1001] = { false, };
int N;
vector<int> v;
queue<int> q;

void dfs(int now) {
	for (int i = 0; i < node[now].size(); i++) { // 현재 노드와 연결된 노드마다
		int n = node[now][i]; // now와 연결된 노드
		if (!check[n]) { // 방문하지 않았다면
			check[n] = true; // 방문 표시
			cout << n << " ";
			dfs(n);
		}
	}
}

void bfs() {
	while (q.size() > 0) {
		int now = q.front(); q.pop();
		for (int i = 0; i < node[now].size(); i++) { // 현재 노드와 연결된 노드마다
			int n = node[now][i]; // now와 연결된 노드
			if (!check[n]) { // 방문하지 않았다면
				q.push(n); // queue에 push
				cout << n << " ";
				check[n] = true; // 방문 표시
			}
		}
	}
}


int main() {

	int M, V; // 정점의 개수, 간선의 개수, 탐색 시작할 정점
	cin >> N >> M >> V;
	
	for (int i = 0; i < M; i++) { // 입력
		int a, b;
		cin >> a >> b;
		node[a].push_back(b);
		node[b].push_back(a);
	}

	for (int i = 0; i <= N; i++)
		sort(node[i].begin(), node[i].end());

	check[V] = true;

	// dfs
	cout << V << " ";
	dfs(V);

	cout << "\n";
	for (int i = 0; i < 1001; i++) // 방문 초기화
		check[i] = false;
	check[V] = true;

	// bfs
	q.push(V);
	cout << V << " ";
	bfs();

	return 0;
}