// https://www.acmicpc.net/problem/1826

#include <iostream>
#include <set>
#include<cstring>
#include<queue>
using namespace std;
int station[10000][2];
priority_queue<int> pq;
int station_num, length, gas,stop=0;

int main() {

	cin >> station_num;

	for (int i = 0; i < station_num; i++)
		cin >> station[i][0] >> station[i][1]; // �Ÿ�, ä�� �� �ִ� ������ ��
	cin >> station[station_num][0] >> gas; // ���������� �Ÿ�, Ʈ���� �ִ� ������ ��

	for (int i = 0; i < station_num; i++) {
		if (i == 0)
			gas -= station[i][0];
		else
			gas -= (station[i][0] - station[i - 1][0]);

		int need = station[i + 1][0] - station[i][0];

		if (need > gas) { // ���� �����ұ��� �� �� ���� ��
			gas += station[i][1]; // ���� ����
			stop++;
			if (need > gas) {
				while (gas < need) {
					if (pq.size() > 0) {
						gas += pq.top();
						pq.pop();
						stop++;
					}
					else {
						cout << "-1";
						return 0;
					}
				}
			}
		}
		else {
			pq.push(station[i][1]); // �������� ���� ���� �� ����
		}

	}

	cout << stop;

	return 0;
}