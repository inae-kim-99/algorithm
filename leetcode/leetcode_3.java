/*
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
    LeetCode 3 : Longest Substring Without Repeating Characters (Difficulty : Medium)

    [문제]
    문자열 s가 주어질 때, 중복된 문자가 없는 가장 긴 문자열의 길이를 구하여라.
    문자열은 영문, 숫자, 기호, 공백으로 구성되어 있음.

    [풀이]
    HashMap을 사용하여 문자가 가장 최근에 나타난 위치를 저장한다. ex) 'a'-> 1
    첫 번째 문자부터 순서대로 확인한다.
    - 현재 문자가 아직 발견되지 않았다면 count++한다.
    - 발견된 문자라면,
      1) (현재 위치 - 전에 발견된 위치)
      2) count + 1
      중에 최소 값을 count에 저장한다.
      이유) 1이 더 크다면, 그 전에 중복된 문자가 있다는 것이기 때문에 현재 상태에서 +1 해야한다.
           2가 더 크다면, 현재 문자가 중복되어 있는 경우이기 때문에 전에 발견된 문자 이후부터 개수를 세야 한다.
 */

import java.util.HashMap;

public class leetcode_3 {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0, count = 0;
        HashMap<Character, Integer> map = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            if (!map.containsKey(s.charAt(i)))
                count++;
            else
                count = Math.min(i - map.get(s.charAt(i)), count + 1);
            map.put(s.charAt(i), i);
            maxLength = Math.max(maxLength, count);
        }

        return maxLength;
    }
}
