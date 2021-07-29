/*
    https://leetcode.com/problems/longest-repeating-character-replacement/
    LeetCode 424 : Longest Repeating Character Replacement (Difficulty : Medium)

    [문제]
    문자열 s, 숫자 k가 주어질 때
    최대 문자 k개를 골라 다른 문자로 바꿀 수 있다.
    이때, 같은 문자들로 이루어진 가장 긴 문자열의 길이를 반환하라.

    [풀이]
    특정 구간에서, 바꿔야 하는 문자의 개수는 (구간의 길이 - 가장 많은 문자의 개수) 이다.

    시작 인덱스, 끝 인덱스를 생성하여 각 구간을 확인한다.
    끝 인덱스로 순서대로 문자를 확인하며 해당 문자의 개수에 +1 한다.

    현재 가장 많은 문자의 개수를 계산하고,
    1) 나머지 문자의 개수가 k보다 크다면 : 해당 구간의 첫 번째 문자의 개수 - 1 하고, 왼쪽을 한 칸 줄인다.
    2) 나머지 문자의 개수가 k보다 작다면 : 현재 구간, 최대 구간 중 최대 값을 다시 저장한다.

 */

public class leetcode_424 {

    public int characterReplacement(String s, int k) {

        int[] letter = new int[26];
        int maxNum = 0, maxLen = 0, otherNum = 0;
        int start = 0, end = 0;

        while (end < s.length()) {
            int endLetter = s.charAt(end) - 'A';
            letter[endLetter]++;

            for (int i = 0; i < letter.length; i++) {
                if (letter[i] > maxNum)
                    maxNum = letter[i];
            }

            otherNum = (end + 1) - (maxNum + start);
            if (otherNum > k) {
                letter[s.charAt(start) - 'A']--;
                start++;
            } else {
                maxLen = Math.max(maxLen, maxNum + otherNum);
            }
            end++;
        }

        return maxLen;
    }

}
