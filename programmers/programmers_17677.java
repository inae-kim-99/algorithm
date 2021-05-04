// https://programmers.co.kr/learn/courses/30/lessons/17677
// 프로그래머스 17677번 : 2018 KAKAO BLIND RECRUITMENT - [1차] 뉴스 클러스터링

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.regex.Pattern;

public class programmers_17677 {


    public static int solution(String str1, String str2) {
        int answer = 0;
        String pattern = "^[a-z]*$";

        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();

        HashMap<String, Integer> firstMap = new HashMap<>();
        HashMap<String, Integer> secondMap = new HashMap<>();
        Set<String> stringSet = new HashSet<>();
        double intersection = 0, union = 0;

        for (int i = 0; i < str1.length() - 1; i++) {
            String str = str1.substring(i, i + 2);
            if (Pattern.matches(pattern, str)) { // 정규 표현식 활용
                if (firstMap.containsKey(str))
                    firstMap.put(str, firstMap.get(str) + 1);
                else {
                    firstMap.put(str, 1);
                    stringSet.add(str);
                }
            }
        }
        for (int i = 0; i < str2.length() - 1; i++) {
            String str = str2.substring(i, i + 2);
            if (Pattern.matches(pattern, str)) { // 정규 표현식 활용
                if (secondMap.containsKey(str))
                    secondMap.put(str, secondMap.get(str) + 1);
                else {
                    secondMap.put(str, 1);
                    stringSet.add(str);
                }
            }
        }

        for (String str : stringSet) {
            if (firstMap.containsKey(str) && secondMap.containsKey(str)) {
                intersection += Math.min(firstMap.get(str), secondMap.get(str));
                union += Math.max(firstMap.get(str), secondMap.get(str));
            } else {
                union += (firstMap.containsKey(str) ? firstMap.get(str) : secondMap.get(str));
            }
        }

        if (union == 0)
            answer = 65536;
        else
            answer = (int) (intersection / union * 65536);

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution("handshake", "shake hands"));
    }

}
