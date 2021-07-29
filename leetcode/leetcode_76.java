/*
    https://leetcode.com/problems/minimum-window-substring/
    LeetCode 76 : Minimum Window Substring (Difficulty : Hard)

    [문제]
    길이가 각각 m과 n인 문자열 s와 t가 주어질 때,
    t의 문자들을 모두 포함하는 m의 최소 크기의 윈도우를 찾아 그 부분 문자열을 반환하라. (중복도 포함)

    [풀이]
    슬라이딩 윈도우 알고리즘을 활용하여 풀어낸다.
    두 포인터 (left, right)를 가지고 left = 0, right = 0부터 시작한다.

    right를 +1씩 움직여가며 탐색하는데, 만약 t를 모두 포함하는 조건이 만족되면
    그 조건 안에서 left를 움직일 수 있는 만큼 +1씩 움직인다.

    HashMap을 활용하여 t의 각 문자의 개수를 모두 포함하는지 확인한다.
 */

import java.util.HashMap;

public class leetcode_76 {

    public static String minWindow(String s, String t) {
        HashMap<Character, Integer> sMap = new HashMap<>();
        HashMap<Character, Integer> tMap = new HashMap<>();

        // t 알파벳 저장
        for (int i = 0; i < t.length(); i++) {
            int num = tMap.getOrDefault(t.charAt(i), 0);
            tMap.put(t.charAt(i), num + 1);
        }

        int minLeft = 0, minRight = Integer.MAX_VALUE;
        int left = 0, right = 0, formed = 0, required = tMap.size();

        while (right < s.length()) {
            // right 늘리기
            char rc = s.charAt(right);
            if (tMap.containsKey(rc)) {
                int num = sMap.getOrDefault(rc, 0);
                sMap.put(rc, num + 1);

                if (sMap.get(rc).equals(tMap.get(rc)))
                    formed++;
            }
            // left 줄이기
            if (formed == required) { // 현재 구간이 t를 포함한다면
                while (left <= right) {
                    char lc = s.charAt(left);
                    if (sMap.containsKey(lc)) {
                        if (sMap.get(lc) > tMap.get(lc)) {
                            sMap.put(lc, sMap.get(lc) - 1);
                        } else
                            break;
                    }
                    left++;
                }
                if (right - left < minRight - minLeft) {
                    minRight = right;
                    minLeft = left;
                }
            }
            right++;
        }

        if(minRight == Integer.MAX_VALUE)
            return "";
        else
            return s.substring(minLeft, minRight + 1);
    }

    public static void main(String[] args) {
        String s = "ADOBECODEBANC";
        String t = "ABC";
        System.out.println(minWindow(s, t));
    }
}
