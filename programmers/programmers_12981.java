// https://programmers.co.kr/learn/courses/30/lessons/12981
// 프로그래머스 12981번 : Summer/Window Coding(2018) - 영어 끝말잇기

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class programmers_12981 {

    public static int[] solution(int n, String[] words) {
        int[] answer = new int[2];

        Set<String> wordSet = new HashSet<>();
        char beforeChar = words[0].charAt(0);
        for (int i = 0; i < words.length; i++) {
            if (beforeChar != words[i].charAt(0) || wordSet.contains(words[i])) {
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                break;
            } else {
                wordSet.add(words[i]);
                beforeChar = words[i].charAt(words[i].length() - 1);
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int n = 3;
        String[] words = {"tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"};
        System.out.println(Arrays.toString(solution(n, words)));
    }

}
