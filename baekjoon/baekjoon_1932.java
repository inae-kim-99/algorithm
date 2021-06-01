// https://www.acmicpc.net/problem/1932
// 백준 1932번 : DP - 정수 삼각형

// 간단 풀이
// 조건 : 아래층에 있는 수는 현채 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
// 해석 : [현재층](i)(j)층에서는 [아래층](i+1)(j) or (i+1)(j+1) 중 하나를 선택할 수 있다.
// -> 이를 아래층의 입장에서 해석해보면 (아래층을 i,j)
//    : (i)(j)층에서는 (i-1)(j) or (i-1)(j-1) 중 하나를 지나올 수 있다.

import java.util.Scanner;

public class baekjoon_1932 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[][] floor = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                floor[i][j] = sc.nextInt();
                floor[i][j] += Math.max(floor[i - 1][j], floor[i - 1][j - 1]);
            }
        }

        int max = 0;
        for (int num : floor[n])
            if (num > max)
                max = num;

        System.out.println(max);
    }
}
