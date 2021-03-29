import java.util.Scanner;

import static java.lang.Integer.min;

public class baekjoon_17485 {

    static int[][] fuel;
    static int[][][] map;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        fuel = new int[N][M]; // 연료 맵
        map = new int[N][M][3]; // 각 위치에 따른 최소 연료를 저장할 배열

        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                fuel[i][j] = sc.nextInt();

        for (int i = 0; i < M; i++)
            for (int j = 0; j < 3; j++)
                map[0][i][j] = fuel[0][i]; // 첫 줄 초기화

        for (int i = 0; i < N; i++) {
            map[i][0][0] = Integer.MAX_VALUE;
            map[i][M - 1][2] = Integer.MAX_VALUE;
        }

        for (int i = 1; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (j != 0)
                    map[i][j][0] = min(map[i - 1][j - 1][1], map[i - 1][j - 1][2]) + fuel[i][j];
                if (j != M - 1)
                    map[i][j][2] = min(map[i - 1][j + 1][0], map[i - 1][j + 1][1]) + fuel[i][j];
                map[i][j][1] = min(map[i - 1][j][0], map[i - 1][j][2]) + fuel[i][j];
            }
        }

        int min = Integer.MAX_VALUE;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < 3; j++) {
                if (map[N - 1][i][j] < min)
                    min = map[N - 1][i][j];
            }
        }
        System.out.println(min);
    }
}
