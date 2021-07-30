/*
    https://leetcode.com/problems/valid-anagram/
    LeetCode 242 : Valid Anagram (Difficulty : Easy)

    [문제]
    문자열 s와 t가 주어질 때, t가 s의 anagram이면 true, 아니면 false를 반환하라.
    * anagram : 주어진 단어나 문자의 순서를 바꾸어 다른 단어나 문장을 만드는 것.

    [풀이]
    주어지는 문자열은 모두 알파벳 소문자로 이루어져 있기 때문에,
    각 알파벳이 몇 개가 존재하는지 확인하고 이를 비교하면 된다.

    알파벳은 총 26개이기 때문에 개수를 저장할 1차원 배열(letters)를 생성하고,
    a ~ z를 인덱스로 나타내기 위해 (알파벳 - 'a')로 나타낸다. (a : 0 ~ z : 25)

    문자열 s를 순서대로 확인하며 letters에 개수를 저장한다.

    그 후 문자열 t를 순서대로 하나씩 탐색하여 letters에서 개수를 뺀다.
    이때, letters[i]의 값이 0인 경우 존재하지 않는 문자가 나타난 것이다.
    이는 anagram이 아니므로 false를 반환한다.

    모두 수행하고 나면 anagram인 것이므로 true를 반환한다.
 */

public class leetcode_242 {

    public static boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        int[] letters = new int[26];
        for (int i = 0; i < s.length(); i++) {
            letters[s.charAt(i) - 'a']++;
        }

        for (int i = 0; i < t.length(); i++) {
            if (letters[t.charAt(i) - 'a'] == 0)
                return false;
            letters[t.charAt(i) - 'a']--;
        }

        return true;

//        HashMap<Character, Integer> sMap = new HashMap<>();
//        for (int i = 0; i < s.length(); i++) {
//            int count = sMap.getOrDefault(s.charAt(i), 0);
//            sMap.put(s.charAt(i), count + 1);
//        }
//
//        for (int i = 0; i < t.length(); i++) {
//            int count = sMap.getOrDefault(t.charAt(i), 0);
//            if (count == 0)
//                return false;
//            sMap.put(t.charAt(i), count - 1);
//        }
//
//        return true;
    }

    public static void main(String[] args) {
        System.out.println(isAnagram("aacc", "ccac"));
    }

}
