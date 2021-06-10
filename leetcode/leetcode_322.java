/*
    https://leetcode.com/problems/coin-change/
    LeetCode 322 : Coin Change (Difficulty : Medium)

    [문제]
    가격이 다른 여러 동전 coins 가 주어질 때,
    amount 가격을 만들기 위해 사용해야 하는 최소 동전의 개수를 구하라.

    [풀이]
    minNums[i] : i원을 만들기 위한 최소 동전 개수
    i원을 만드는 최소 동전의 개수는
    (i - 동전의 가격 중 하나)를 만드는 최소 동전 개수에 1을 더하면 된다.
*/

import java.util.Arrays;

public class leetcode_322 {
    public int coinChange(int[] coins, int amount) {

        int[] minNums = new int[amount + 1];
        Arrays.fill(minNums, amount + 1);
        minNums[0] = 0;
        Arrays.sort(coins);

        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i - coin >= 0) {
                    minNums[i] = Math.min(minNums[i], minNums[i - coin]);
                } else {
                    break;
                }
            }
            minNums[i]++;
        }

        return minNums[amount] > amount ? -1 : minNums[amount];
    }
}
