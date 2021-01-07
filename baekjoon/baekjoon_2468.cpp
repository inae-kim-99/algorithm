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

    if (visited[y][x]) // 이미 방문한 지역인 경우
        return;

    visited[y][x] = true; // 방문 체크
   
    for (int i = 0; i < 4; i++) { // 상하좌우 탐색
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx >= 0 && nx < N && ny >= 0 && ny < N) // 경계 안
            if (area[ny][nx] > h) // 안전 영역일 때 탐색
                dfs(nx, ny, h);
    }
}

int main() {

    set<int> rain_list;
    int max = 1;

    // 입력
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> area[i][j];
            rain_list.insert(area[i][j]);
        }
    }

    //비의 양에 따라
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