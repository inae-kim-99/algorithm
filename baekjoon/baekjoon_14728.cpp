#include <iostream>
#include <vector>
using namespace std;
int N, T;
int dp[101][100001];
pair<int, int> value[101];

int main() {

	cin >> N >> T;

	for (int i = 1; i <= N; i++)
		cin >> value[i].first >> value[i].second; // first : 예상 공부 시간, second : 배점

	for (int i = 1; i <= N; i++) {
		for (int limit = 1; limit <= T; limit++) {
			dp[i][limit] = dp[i - 1][limit]; 
			if (value[i].first <= limit && (dp[i-1][limit - value[i].first] + value[i].second) > dp[i][limit]) { // i-1번째까지의 값과 i를 담은 값을 비교
				dp[i][limit] = dp[i - 1][limit - value[i].first] + value[i].second;
			}
		}
	}

	cout << dp[N][T];

	return 0;
}