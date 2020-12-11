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
	for (int i = 0; i < node[now].size(); i++) { // ���� ���� ����� ��帶��
		int n = node[now][i]; // now�� ����� ���
		if (!check[n]) { // �湮���� �ʾҴٸ�
			check[n] = true; // �湮 ǥ��
			cout << n << " ";
			dfs(n);
		}
	}
}

void bfs() {
	while (q.size() > 0) {
		int now = q.front(); q.pop();
		for (int i = 0; i < node[now].size(); i++) { // ���� ���� ����� ��帶��
			int n = node[now][i]; // now�� ����� ���
			if (!check[n]) { // �湮���� �ʾҴٸ�
				q.push(n); // queue�� push
				cout << n << " ";
				check[n] = true; // �湮 ǥ��
			}
		}
	}
}


int main() {

	int M, V; // ������ ����, ������ ����, Ž�� ������ ����
	cin >> N >> M >> V;
	
	for (int i = 0; i < M; i++) { // �Է�
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
	for (int i = 0; i < 1001; i++) // �湮 �ʱ�ȭ
		check[i] = false;
	check[V] = true;

	// bfs
	q.push(V);
	cout << V << " ";
	bfs();

	return 0;
}