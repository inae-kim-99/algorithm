/*
    https://leetcode.com/problems/word-break/
    LeetCode 139 : Word Break (Difficulty : Medium)

    [문제]
    s(문자열)와 wordDict(단어리스트)가 주어질 때,
    s를 wordDict의 단어로 구성할 수 있으면 true, 없으면 false를 리턴하라.
    단어는 여러번 사용할 수 있다.

    [풀이]
    q : s의 인덱스들을 저장할 큐
    exist[i] : 방문한 인덱스이면 true, 방문하지 않았으면 false 저장

    q에 단어를 시작할 수 있는 index를 저장한다. 처음에 0을 저장해 놓는다.
    q의 index를 하나 빼서, s(문자열)의 index부터 시작할 수 있는 단어를 찾는다.
    단어가 있다면 index에서 그 단어의 길이를 더하고 다음 index를 q에 저장한다. (-> nextIndex)
    만약 nextIndex가 s(문자열)의 길이라면 단어들로 구성할 수 있음을 나타내므로 true를 리턴한다.
*/

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class leetcode_139 {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] exist = new boolean[s.length()];
        Queue<Integer> q = new LinkedList<>();
        q.add(0);

        while (!q.isEmpty()) {
            int index = q.poll();
            for (String word : wordDict) {
                if (s.substring(index).startsWith(word)) {
                    int nextIndex = index + word.length();

                    if (nextIndex == s.length())
                        return true;

                    if (!exist[nextIndex]) {
                        q.add(nextIndex);
                        exist[nextIndex] = true;
                    }
                }
            }
        }
        return false;
    }
}
