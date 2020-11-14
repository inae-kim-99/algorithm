#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Robot {
	int x;
	int y;
	int direct;
};

int main() {

	int A, B, N, M;
	vector<Robot> robotList;
	vector<pair<int, int>> answer;

	cin >> A >> B >> N >> M;

	//�� �κ����� �ʱ���ġ, ����
	for (int i = 0; i < N; i++) {
		int x, y,direct;
		char d;
		cin >> x >> y >> d;

		if (d == 'N')
			direct = 0;
		else if (d == 'E')
			direct = 1;
		else if (d == 'S')
			direct = 2;
		else
			direct = 3;

		Robot r = { x,y,direct };
		robotList.push_back(r);
		//cout << robotList.size() << endl;

	}

	//���
	for (int i = 0; i < M; i++) {
		int idx, repeat;
		char order;
		cin >> idx >> order >> repeat;
		if (order == 'L') {
			if (robotList[idx - 1].direct - repeat%4 <= 0) {
				robotList[idx - 1].direct = robotList[idx - 1].direct - repeat % 4 + 4;
			}
			else {
				robotList[idx - 1].direct -= repeat;
			}
		}
		else if (order == 'R') {
			if (robotList[idx - 1].direct + repeat % 4 > 3) {
				robotList[idx - 1].direct -= 4;
			}
			else {
				robotList[idx - 1].direct += repeat % 4;
			}
		}
		else {
			int dx, dy;
			if (robotList[idx-1].direct ==0) { // y������
				dx = 0;
				dy = 1;
			}
			else if (robotList[idx - 1].direct == 2) { // y����Ʒ�
				dx = 0;
				dy = -1;
			}
			else if (robotList[idx - 1].direct == 1) { // x ������
				dx = 1;
				dy = 0;
			}
			else { // ����
				dx = -1;
				dy = 0;
			}
			for (int k = 0; k < repeat; k++) {
				robotList[idx - 1].x += dx;
				robotList[idx - 1].y += dy;
				if (robotList[idx - 1].x == 0 || robotList[idx - 1].x == A
					|| robotList[idx-1].y == 0 || robotList[idx - 1].y == B) {
					cout << "Robot " << idx << " crashes into the wall" << endl;
					return 0;
				}
				else {
					for (int u = 0; u < robotList.size(); u++) {
						if (idx-1 != u && robotList[u].x == robotList[idx - 1].x && robotList[u].y == robotList[idx - 1].y) {
							cout << "Robot " << idx << " crashes into robot " << u+1<<endl;
							return 0;
						}
					}
				}
			}
		}
	}
	cout << "OK" << endl;
	return 0;
}

