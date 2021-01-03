#include <iostream>
#include <set>
#include<cstring>
using namespace std;
int N;
int area[100][100];
bool visited[100][100];
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

void dfs(int x, int y,int h) {

    if (visited[y][x]) // �̹� �湮�� ������ ���
        return;

    visited[y][x] = true; // �湮 üũ
   
    for (int i = 0; i < 4; i++) { // �����¿� Ž��
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx >= 0 && nx < N && ny >= 0 && ny < N) // ��� ��
            if (area[ny][nx] > h) // ���� ������ �� Ž��
                dfs(nx, ny, h);
    }
}

int main() {

    set<int> rain_list;
    int max = 1;

    // �Է�
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> area[i][j];
            rain_list.insert(area[i][j]);
        }
    }

    //���� �翡 ����
    for (set<int>::iterator rain = rain_list.begin(); rain != rain_list.end(); ++rain) {
        memset(visited, false, sizeof(visited));
        int count = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (area[i][j] > *rain && !visited[i][j]) {
                    dfs(j,i,*rain);
                    count++;
                }
            }
        }
        //cout << "rain : " << *rain << ", count : " << count << endl;
        if (count > max)
            max = count;
    }

    cout << max;

    return 0;
}