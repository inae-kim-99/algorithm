// https://www.acmicpc.net/problem/2579
// 백준 2579번 : DP - 계단 오르기

// 간단 풀이
// 각 계단의 점수를 입력 받고, (i)계단에서 (i-1)계단에서의 최대 점수와 (i-2)계단에서의 최대 점수를 저장한다.
// 단, (i-1)계단에서 그 (i-2)계단을 밟고 온 경우는 (i)계단을 밟을 수 없으므로 -> 연속 3개 계단을 밟는 경우!
// 그 경우는 제외한다.

import java.util.Scanner;

public class backjoon_2579 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[][] stairs = new int[n + 2][2];
        stairs[0][0] = stairs[0][1] = stairs[1][0] = stairs[1][1] = 0;
        for (int i = 2; i <= n + 1; i++) {
            int num = sc.nextInt();
            stairs[i][0] = num + Math.max(stairs[i - 2][0], stairs[i - 2][1]);
            stairs[i][1] = num + stairs[i - 1][0];
        }

        System.out.println(Math.max(stairs[n + 1][0], stairs[n + 1][1]));
    }
}
