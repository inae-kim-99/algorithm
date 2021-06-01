// https://programmers.co.kr/learn/courses/30/lessons/42862
// 프로그래머스 42862번 : 탐욕법(Greedy) - 체육복

import java.util.Arrays;

public class programmers_42862 {

    public static int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int[] students = new int[n + 2];
        Arrays.fill(students, 1);

        for (int l : lost)
            students[l] -= 1;
        for (int r : reserve)
            students[r] += 1;

        for (int i = 1; i <= n; i++) {
            if (students[i] == 0) {
                if (students[i - 1] == 2)
                    students[i - 1] -= 1;
                else if (students[i + 1] == 2)
                    students[i + 1] -= 1;
                else
                    answer += 1;
            }
        }

        return n - answer;
    }

    public static void main(String[] args) {
        int[] l = {2,4};
        int[] r = {1,3,5};
        System.out.println(solution(5,l,r));
    }
}
