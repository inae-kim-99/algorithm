// https://programmers.co.kr/learn/courses/30/lessons/42889
// 프로그래머스 42889번 : 2019 KAKAO BLIND RECRUITMENT - 실패율

import java.util.ArrayList;
import java.util.Collections;

public class programmers_42889 {

    class Stage implements Comparable<Stage> {
        int level;
        double rate;

        Stage(int l, double r) {
            level = l;
            rate = r;
        }

        @Override
        public int compareTo(Stage stage) {
            if (rate < stage.rate)
                return 1;
            else if (rate > stage.rate)
                return -1;
            else
                return (level < stage.level ? -1 : 1);
        }
    }

    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        double[] fail = new double[N];
        int len = stages.length;

        for (int level = 0; level < N; level++) { // 스테이지마다
            for (int player = 0; player < len; player++) { // 플레이어마다
                if (stages[player] == level + 1)// 클리어하지 못한 경우
                    fail[level] += 1;
                if (stages[player] > level + 1) // 클리어한 경우
                    answer[level] += 1;
            }
        }

        ArrayList<Stage> list = new ArrayList<>();
        for (int i = 1; i <= N; i++)
            list.add(new Stage(i + 1, fail[i] / answer[i]));

        Collections.sort(list);

        for (int i = 0; i < N; i++)
            answer[i] = list.get(i).level;

        return answer;
    }
}
