#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;
int prefer[500];

int main() {

	int N, K; 
	cin >> N >> K;
	for (int i = 0; i < N; i++)
		cin >> prefer[i];
	
	double min = 1000000000;
	while (K < N) {
		for (int i = 0; i < N - K + 1; i++) { // 1씩 이동하며 모두 확인
		// 평균 계산
			double mean = 0;
			for (int j = i; j < i + K; j++)
				mean += prefer[j];
			mean /= K;
			// 분산 계산
			double variance = 0;
			for (int j = i; j < i + K; j++)
				variance += pow(mean - prefer[j], 2);
			variance /= K;
			if (variance < min)
				min = variance;
		}
		K++;
	}
	
	cout << fixed;
	cout.precision(7);
	cout << sqrt(min);
	return 0;
}