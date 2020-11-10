#include <iostream>
#include <vector>
using namespace std;

long long dp[31][31];

long long calculate(int one, int half) {

	if (dp[one][half] != 0) { // �̹� ���� ���̸�
		return dp[one][half];
	}

	if (one == 0) // ���� ���� ��� �ݾ��̸�
		return 1;

	if (half == 0) {
		return dp[one][half] = calculate(one - 1, 1);
	}
	else {
		return dp[one][half] = calculate(one - 1, half + 1) + calculate(one, half - 1);
	}

}

void main() {

	int N;
	vector<long long> ans;

	while (true) {

		cin >> N;

		if (N == 0) // �Է��� ������ ��
			break;

		ans.push_back(calculate(N - 1, 1));

	}

	for (int i = 0; i < ans.size(); i++)
		cout << ans[i] << "\n";
}