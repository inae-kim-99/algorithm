#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Ball {
	int x, y, type;
	Ball(int _x, int _y, int _type) : x(_x), y(_y), type(_type) {};
};

const int BLUE = 1, RED = 2, HOLE = 3, EMPTY = 4,WALL=5;
int dx[4] = { 0,0,-1,1 }; // 위, 아래, 왼쪽, 오른쪽
int dy[4] = { -1,1,0,0 };
int num = 11;

bool compare_descend_x(const Ball& a, const Ball& b) { // x 내림차순
	return a.x > b.x;
}

bool compare_ascend_x(const Ball& a, const Ball& b) { // x 오름차순
	return a.x < b.x;
}

bool compare_descend_y(const Ball& a, const Ball& b) { // y 내림차순
	return a.y > b.y;
}

bool compare_ascend_y(const Ball& a, const Ball& b) { // y 오름차순
	return a.y < b.y;
}

void game(vector<vector<int>> board,  vector<Ball> ball_list, int direction, int count) {

	if (count == 11) // 10번 초과는 return
		return;

	if (direction == 0) // 위로 기울이기 (위에 있는 공 순서대로)
		sort(ball_list.begin(), ball_list.end(), compare_ascend_y);
	else if(direction == 1) // 아래로 기울이기 (아래에 있는 공 순서대로)
		sort(ball_list.begin(), ball_list.end(), compare_descend_y);
	else if(direction == 2) // 왼쪽으로 기울이기 (왼쪽에 있는 공 순서대로)
		sort(ball_list.begin(), ball_list.end(), compare_ascend_x);
	else // 오른쪽으로 기울이기 (오른쪽에 있는 공 순서대로)
		sort(ball_list.begin(), ball_list.end(), compare_descend_x);

	bool move = false;
	bool success = false;

	for (int i = 0; i < ball_list.size(); i++) {
		for (int j = 1;; j++) {

			int ball_x = ball_list[i].x + dx[direction] * j;
			int ball_y = ball_list[i].y + dy[direction] * j;
			int locate = board[ball_y][ball_x];

			if (locate == HOLE) { // 공의 위치가 구멍일 때
				if (ball_list[i].type == RED) { // 빠진 공이 red
					success = true;
					move = false;
					board[ball_list[i].y][ball_list[i].x] = EMPTY;
					break;
				}	
				else { // 빠진 공이 blue
					success = false;
					move = false;
					board[ball_list[i].y][ball_list[i].x] = EMPTY;
					break;
				}
			}
			else if (locate == WALL || locate == RED || locate == BLUE) { // 더 움직일 수 없을 때
				board[ball_list[i].y][ball_list[i].x] = EMPTY;
				ball_list[i].x += dx[direction] * (j - 1);
				ball_list[i].y += dy[direction] * (j - 1);
				board[ball_list[i].y][ball_list[i].x] = ball_list[i].type;
				break;
			}
			move = true;
		}
		//cout <<"ball : "<< ball_list[i].y << ", " << ball_list[i].x <<" ("<<ball_list[i].type<<")"<< endl;
	}

	if (success) {
		if (count < num) {
				num = count;
				//cout << direction << ", " << count << endl;
		}
		return;
	}

	if (move) {
		for (int i = 0; i < 4; i++) {
			if (direction == 0 || direction == 2) { // 0(위), 2(왼) 인 경우, 각각 1(아래), 3(오른) 방향 불가 
				if (direction+1 != i)
					game(board, ball_list, i, count + 1);
			}
			else { // 1(아래), 3(오른) 인 경우, 각각 0(위), 2(왼) 방향 불가 
				if (direction - 1 != i)
					game(board, ball_list, i, count + 1);
			}
		}
	}
}

int main() {

	int board_x, board_y;
	cin >> board_y >> board_x;


	vector<vector<int>> board;
	vector<Ball> ball_list;
	vector<int> v; v.assign(board_x, WALL);
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
					ball_list.push_back(Ball(j, i, BLUE));
					board[i][j] = BLUE;
					break;
				case 'R':
					ball_list.push_back(Ball(j, i, RED));
					board[i][j] = RED;
					break;
				case 'O':
					board[i][j] = HOLE;
					break;
				case '#':
					board[i][j] = WALL;
				}
			}
		}
	}

	for (int i = 0; i < 4; i++) {
		game(board, ball_list, i, 1);
	}

	if (num == 11)
		cout << "-1";
	else
		cout << num;

	return 0;
}