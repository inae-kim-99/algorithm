// https://www.acmicpc.net/problem/1003
// 백준 1003 : 피보나치 함수

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class baekjoon_1003 {

    static int[] dp0, dp1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        dp0 = new int[41];
        dp1 = new int[41];

        dp0[0] = 1;
        dp0[1] = 0;
        dp1[0] = 0;
        dp1[1] = 1;

        for (int i = 2; i < 41; i++) {
            dp0[i] = dp0[i - 1] + dp0[i - 2];
            dp1[i] = dp1[i - 1] + dp1[i - 2];
        }

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int num = Integer.parseInt(br.readLine());
            System.out.println(dp0[num] + " " + dp1[num]);
        }
    }
}
