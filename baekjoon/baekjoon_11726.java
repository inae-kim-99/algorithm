// https://www.acmicpc.net/problem/11726
// 백준 11726번 : 2*n 타일링

import java.util.Scanner;

public class baekjoon_11726 {

    static int[] way;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        way = new int[n + 1];
        way[0] = way[1] = 1;
        for (int i = 2; i <= n; i++) {
            way[i] = (way[i - 1] + way[i - 2]) % 10007;
        }

        System.out.println(way[n]);
    }
}
