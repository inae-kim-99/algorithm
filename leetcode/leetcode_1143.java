/*
    https://leetcode.com/problems/longest-common-subsequence/
    LeetCode 1143 : Longest Common Subsequence (Difficulty : Medium)

    [문제]
    두 문자열 text1, text2가 주어질 때,
    the length of their longest common subsequence를 구하여라.
    (가장 긴 공통된 문자열을 구하라. 순서 변경은 불가, 문자 생략은 가능)

    [풀이]
    두 문자열의 문자를 하나 하나 비교하며 가장 최대 길이를 구한다.
    인덱스 i, j 를 만들어 text1[i], text2[j]를 비교한다.
    (i, j) 문자가 같은 경우 : (i-1, j-1)까지의 길이 + 1를 저장한다.
    (i, j) 문자가 다른 경우 : (i-1, j)과 (i, j-1) 중에 최대 길이를 저장한다.
    모두 계산하면 (size1, size2)에 저장한 길이가 가장 최대 길이가 된다.
*/

public class leetcode_1143 {
    public int longestCommonSubsequence(String text1, String text2) {

        int size1 = text1.length(), size2 = text2.length();
        int[][] dp = new int[size1+1][size2+1];

        for(int i=0;i<size1;i++){
            for(int j=0;j<size2;j++){
                if(text1.charAt(i) == text2.charAt(j))
                    dp[i+1][j+1] = dp[i][j] + 1;
                else
                    dp[i+1][j+1] = Math.max(dp[i+1][j], dp[i][j+1]);
            }
        }

        return dp[size1][size2];
    }
}
