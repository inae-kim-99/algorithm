// https://www.acmicpc.net/problem/1149
// 백준 1149번 : RGB 거리

import java.io.IOException;
import java.util.Scanner;

public class baekjoon_1149 {

    static final int RED = 0, BLUE = 1, GREEN = 2;
    static int[][] sumWeights, weights;

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine());
        sumWeights = new int[N][3];
        weights = new int[N][3];

        // weight 입력
        for (int i = 0; i < N; i++) {
            String[] str = sc.nextLine().split(" ");
            for (int j = 0; j < 3; j++)
                weights[i][j] = Integer.parseInt(str[j]);
        }

        // 첫번째 sumWeight 대입
        sumWeights[0][RED] = weights[0][RED];
        sumWeights[0][BLUE] = weights[0][BLUE];
        sumWeights[0][GREEN] = weights[0][GREEN];

        // 현재 집에 색칠할 색의 비용과 이전 집까지의 비용의 최솟값을 합하여 계산
        for (int i = 1; i < N; i++) {
            sumWeights[i][RED] = Math.min(sumWeights[i-1][BLUE],sumWeights[i-1][GREEN])+weights[i][RED];
            sumWeights[i][BLUE] = Math.min(sumWeights[i-1][RED],sumWeights[i-1][GREEN])+weights[i][BLUE];
            sumWeights[i][GREEN] = Math.min(sumWeights[i-1][RED],sumWeights[i-1][BLUE])+weights[i][GREEN];
        }

        // 최솟값 계산
        int min = Math.min(sumWeights[N - 1][RED], sumWeights[N - 1][BLUE]);
        min = Math.min(min, sumWeights[N - 1][GREEN]);

        System.out.println(min);
    }
}
