// https://www.acmicpc.net/problem/2839
// 2839번 설탕 배달

import java.util.Scanner;

public class baekjoon_2839 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int num_5kg = 0;
        int num_3kg = 0;

        while (N > 0) {
            if (N % 5 == 0) {
                num_5kg = N / 5;
                N = 0;
                break;
            } else {
                N -= 3;
                num_3kg += 1;
            }
        }

        if(N == 0)
            System.out.println(num_3kg+num_5kg);
        else
            System.out.println("-1");
    }
}
