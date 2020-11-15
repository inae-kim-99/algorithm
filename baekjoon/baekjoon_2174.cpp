#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Robot {
	int x, y, dir;
};

int main() {

	int A, B, N, M;
	vector<Robot> robotList;
	vector<pair<int, int>> answer;

	cin >> A >> B >> N >> M;

	//각 로봇들의 초기위치, 방향
	for (int i = 0; i < N; i++) {
		int x, y,dir;
		char d;
		cin >> x >> y >> d;

		if (d == 'N')
			dir = 0;
		else if (d == 'E')
			dir = 1;
		else if (d == 'S')
			dir = 2;
		else
			dir = 3;

		Robot r = { x,y,dir };
		robotList.push_back(r);
		//cout << robotList.size() << endl;

	}

	//명령
	for (int i = 0; i < M; i++) {

		int idx, repeat;
		char order;
		cin >> idx >> order >> repeat;

		if (order == 'L') {
			robotList[idx - 1].dir -= repeat % 4;
			if (robotList[idx - 1].dir < 0)
				robotList[idx - 1].dir += 4;
		}
		else if (order == 'R') {
			robotList[idx - 1].dir += repeat % 4;
			if (robotList[idx - 1].dir > 3)
				robotList[idx - 1].dir -= 4;
		}
		else {
			int dx, dy;
			if (robotList[idx-1].dir ==0) { // y방향위
				dx = 0;
				dy = 1;
			}
			else if (robotList[idx - 1].dir == 2) { // y방향아래
				dx = 0;
				dy = -1;
			}
			else if (robotList[idx - 1].dir == 1) { // x 오른쪽
				dx = 1;
				dy = 0;
			}
			else { // 왼쪽
				dx = -1;
				dy = 0;
			}
			for (int k = 0; k < repeat; k++) {
				robotList[idx - 1].x += dx;
				robotList[idx - 1].y += dy;
				if (robotList[idx - 1].x == 0 || robotList[idx - 1].x > A
					|| robotList[idx-1].y == 0 || robotList[idx - 1].y > B) {
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

