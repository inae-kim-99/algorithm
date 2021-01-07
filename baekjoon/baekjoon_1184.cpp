#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Ball {
	int x, y, type;
	Ball(int _x, int _y, int _type) : x(_x), y(_y), type(_type) {};
};

const int BLUE = 1, RED = 2, HOLE = 3, EMPTY = 4,WALL=5;
int dx[4] = { 0,0,-1,1 }; // ��, �Ʒ�, ����, ������
int dy[4] = { -1,1,0,0 };
int num = 11;

bool compare_descend_x(const Ball& a, const Ball& b) { // x ��������
	return a.x > b.x;
}

bool compare_ascend_x(const Ball& a, const Ball& b) { // x ��������
	return a.x < b.x;
}

bool compare_descend_y(const Ball& a, const Ball& b) { // y ��������
	return a.y > b.y;
}

bool compare_ascend_y(const Ball& a, const Ball& b) { // y ��������
	return a.y < b.y;
}

void game(vector<vector<int>> board,  vector<Ball> ball_list, int direction, int count) {

	if (count == 11) // 10�� �ʰ��� return
		return;

	if (direction == 0) // ���� ����̱� (���� �ִ� �� �������)
		sort(ball_list.begin(), ball_list.end(), compare_ascend_y);
	else if(direction == 1) // �Ʒ��� ����̱� (�Ʒ��� �ִ� �� �������)
		sort(ball_list.begin(), ball_list.end(), compare_descend_y);
	else if(direction == 2) // �������� ����̱� (���ʿ� �ִ� �� �������)
		sort(ball_list.begin(), ball_list.end(), compare_ascend_x);
	else // ���������� ����̱� (�����ʿ� �ִ� �� �������)
		sort(ball_list.begin(), ball_list.end(), compare_descend_x);

	bool move = false;
	bool success = false;

	for (int i = 0; i < ball_list.size(); i++) {
		for (int j = 1;; j++) {

			int ball_x = ball_list[i].x + dx[direction] * j;
			int ball_y = ball_list[i].y + dy[direction] * j;
			int locate = board[ball_y][ball_x];

			if (locate == HOLE) { // ���� ��ġ�� ������ ��
				if (ball_list[i].type == RED) { // ���� ���� red
					success = true;
					move = false;
					board[ball_list[i].y][ball_list[i].x] = EMPTY;
					break;
				}	
				else { // ���� ���� blue
					success = false;
					move = false;
					board[ball_list[i].y][ball_list[i].x] = EMPTY;
					break;
				}
			}
			else if (locate == WALL || locate == RED || locate == BLUE) { // �� ������ �� ���� ��
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
			if (direction == 0 || direction == 2) { // 0(��), 2(��) �� ���, ���� 1(�Ʒ�), 3(����) ���� �Ұ� 
				if (direction+1 != i)
					game(board, ball_list, i, count + 1);
			}
			else { // 1(�Ʒ�), 3(����) �� ���, ���� 0(��), 2(��) ���� �Ұ� 
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