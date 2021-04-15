// https://programmers.co.kr/learn/courses/30/lessons/42840
// 프로그래머스 42840번 : 완전탐색 - 모의고사

import java.util.Vector;

public class programmers_42840 {
    public int[] solution(int[] answers) {
        int[][] way = {{1, 2, 3, 4, 5},
                {2, 1, 2, 3, 2, 4, 2, 5},
                {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
        };
        int[] score = {0, 0, 0};

        for (int i = 0; i < answers.length; i++) {
            for (int j = 0; j < 3; j++) {
                if (answers[i] == way[j][i % way[j].length])
                    score[j] += 1;
            }
        }

        int max = Math.max(Math.max(score[0], score[1]), score[2]);

        Vector<Integer> nums = new Vector<>();
        for (int i = 0; i < 3; i++)
            if (max == score[i])
                nums.add(i + 1);

        int[] answer = new int[nums.size()];
        for (int i = 0; i < nums.size(); i++)
            answer[i] = nums.get(i);

        return answer;
    }
}
