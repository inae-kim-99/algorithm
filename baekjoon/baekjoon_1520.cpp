#include <iostream>
using namespace std;
int height, width;
int area[500][500];
int way[500][500];
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1, -1, 0,0 };

int findWay(int y, int x) {
	// �������
	if (y >= height || y < 0 || x >= width || x < 0) // ���� ��Ż
		return 0;
	else if (y == height - 1 && x == width - 1) // ������ ����
		return 1;
	else if (way[y][x] != -1) // �̹� Ž���ߴ� ������ ���
		return way[y][x];
	// Ž��
	int count = 0;
	int before = area[y][x];
	way[y][x] = 0;
	for (int i = 0; i < 4; i++) {
		int sy = y + dy[i];
		int sx = x + dx[i];
		if (area[sy][sx] < before) {
			count += findWay(sy, sx);
		}
	}
	way[y][x] = count;
	return count;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	//�Է�
	cin >> height >> width;

	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++) {
			cin >> area[i][j];
			way[i][j] = -1;
		}
	}

	cout << findWay(0, 0);

	return 0;
}