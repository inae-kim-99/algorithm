/*
    https://leetcode.com/problems/group-anagrams/
    LeetCode 49 : Group Anagrams (Difficulty : Medium)

    [문제]
    문자열들을 담고 있는 1차원 배열(strs)이 주어질 때,
    같은 anagram들을 그룹지어라. 순서는 상관 없음.
    * anagram : 주어진 단어나 문자의 순서를 바꾸어 다른 단어나 문장을 만드는 것.

    [풀이]
    단어를 char 배열로 바꾸어 오름차순 정렬을 하면, anagram들은 모두 같은 단어가 된다.

    각 단어를 순서대로 확인한다.
    오름차순으로 정렬된 단어가 처음 발견된 단어라면, (정렬된 단어, 해당 단어를 추가한 새 리스트)를 맵에 추가한다.
    이미 존재하는 단어라면, (정렬된 단어)를 맵의 키로 접근하여 해당 리스트에 추가한다.

    그 후, map의 value를 리스트로 변환하여 반환한다.

 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class leetcode_49 {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sortedStr = Arrays.toString(chars);

            if (map.containsKey(sortedStr)) {
                map.get(sortedStr).add(str);
            } else {
                List<String> list = new ArrayList<>();
                list.add(str);
                map.put(sortedStr, list);
            }
        }

        return new ArrayList<>(map.values());
    }
}
