// https://www.acmicpc.net/problem/2178
// 백준 2178번 : 그래프이론 - 미로 탐색

// 간단 풀이
// Queue를 활용하여 문제를 해결!
// 큐에 시작점(0,0)를 넣고 큐가 비어있을 때까지 아래를 반복한다.
// - 큐에서 맨 앞에 있는 요소를 빼서 확인하고, 그 점에서 갈 수 있는 위치를 다시 큐에 넣는다.
// - 단, countMap에 현재 위치까지 지나온 칸의 수를 저장하기 때문에, countMap이 0이 아니면 탐색하지 않는다.

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class baekjoon_2178 {

    final static int[][] DIRECTION = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}}; // 0,1,2,3
    static int N, M;
    static String[] map;
    static int[][] countMap;

    static void bfs() {
        Queue<Location> q = new LinkedList<>();
        q.add(new Location(0, 0));
        countMap[0][0] = 1;

        while (!q.isEmpty()) {

            Location loc = q.poll();

            for (int i = 0; i < 4; i++) { // 상하좌우 4 방향

                int nx = loc.x + DIRECTION[i][0];
                int ny = loc.y + DIRECTION[i][1];

                if (nx >= 0 && nx < M && ny >= 0 && ny < N
                        && map[ny].charAt(nx) == '1'
                        && countMap[ny][nx] == 0) { // 지나갈 수 있는 칸이고 아직 방문하지 않은 칸인 경우
                    countMap[ny][nx] = countMap[loc.y][loc.x] + 1; // 지나온 칸의 횟수 + 1
                    q.add(new Location(nx, ny));
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] num = sc.nextLine().split(" ");
        N = Integer.parseInt(num[0]);
        M = Integer.parseInt(num[1]);
        map = new String[N];
        countMap = new int[N][M];

        for (int i = 0; i < N; i++)
            map[i] = sc.nextLine();

        bfs();

        System.out.println(countMap[N - 1][M - 1]);
    }

    static class Location {
        int x;
        int y;

        Location(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}


