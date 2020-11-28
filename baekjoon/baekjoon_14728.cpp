#include <iostream>
#include <vector>
using namespace std;
int N, T;
int dp[101][100001];
pair<int, int> value[101];

int main() {

	cin >> N >> T;

	for (int i = 1; i <= N; i++)
		cin >> value[i].first >> value[i].second; // first : ���� ���� �ð�, second : ����

	for (int i = 1; i <= N; i++) {
		for (int limit = 1; limit <= T; limit++) {
			dp[i][limit] = dp[i - 1][limit]; 
			if (value[i].first <= limit && (dp[i-1][limit - value[i].first] + value[i].second) > dp[i][limit]) { // i-1��°������ ���� i�� ���� ���� ��
				dp[i][limit] = dp[i - 1][limit - value[i].first] + value[i].second;
			}
		}
	}

	cout << dp[N][T];

	return 0;
}