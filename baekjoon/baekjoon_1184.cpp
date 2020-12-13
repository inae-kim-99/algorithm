#include <iostream>
#include <vector>
using namespace std;
vector<vector<int>> board;
vector<Ball> ball_list;
const int BLUE = 1, RED = 2, HOLE = 3, EMPTY = 4;
int board_x, board_y;
int dx[4] = { 0,0,-1,1 }; // 위, 아래, 왼쪽, 오른쪽
int dy[4] = { -1,1,0,0 };

struct Ball {
	int x, y, type;
	Ball(int _x, int _y, int _type) : x(_x), y(_y), type(_type) {};
};

bool compare_x(const pair<int, int>& a, const pair<int, int>& b) {
	return a.second > b.second;
}

bool compare_y(const pair<int, int>& a, const pair<int, int>& b) {
	return a.first > b.first;
}

int game(int direction) {

	// 오른쪽으로 기울이기
	
}

int main() {

	cin >> board_y >> board_x;

	vector<int> v; v.assign(board_x, -1);
	board.assign(board_y, v);

	for (int i = 0; i < board_y; i++) {
		string row;
		cin >> row;
		if (i != 0 && i != board_y - 1) {
			for (int j = 1; j < board_x - 1; j++) {
				switch (row[j]) {
				case '.':
					board[i][j] = EMPTY;
					break;
				case 'B':
					board[i][j] = BLUE;
					ball_list.push_back(Ball(j, i, BLUE));
					break;
				case 'R':
					board[i][j] = RED;
					ball_list.push_back(Ball(j, i, RED));
					break;
				case 'O':
					board[i][j] = HOLE;
					break;
				}
			}
		}
	}





	return 0;
}