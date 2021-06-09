/*
    https://leetcode.com/problems/climbing-stairs/
    LeetCode 70 : Climbing Stairs (Difficulty : Easy)
    
    [문제]
    n개의 계단이 있을 때, 한 번에 1개 또는 2개의 계단을 올라갈 수 있다.
    꼭대기에 오르기까지 계단을 오르는 방법이 몇 가지 인가?

    [풀이]
    n번 째 계단에 도달하기 위해서는
    1) n-1번 째 계단에서 1개의 계단을 오르기
    2) n-2번 째 계단에서 2개의 계단을 오르기
    위 2가지 방법이 있으므로, 이를 1개부터 n개 까지 순서대로 저장해 나간다.
*/

public class leetcode_70 {

    public int climbStairs(int n) {

        int[] ways = new int[n + 1];    // ways[i] : i번 째 계단을 오르는 방법의 수
        ways[0] = ways[1] = 1;

        for (int i = 2; i <= n; i++)
            ways[i] = ways[i - 1] + ways[i - 2];

        return ways[n];
    }

}
