/*
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    LeetCode : Best Time to Buy and Sell Stock (Difficulty : Easy)

    [문제]
    물건을 구매하고 되파는데 최대의 이익은 얼마인가?

    [간단 풀이]
    profit : 최대 이익
    min : 최소 price
    prices[i] 와 min 과의 차이가 profit 보다 큰 경우 그 차이 값을 profit 에 저장한다.
    이후 prices[i] 가 min 보다 작은 경우 그 값을 min 에 저장한다.
*/

public class leetcode_121 {
    public int maxProfit(int[] prices) {

        int profit = 0;
        int min = prices[0];

        for (int i = 1; i < prices.length; i++) {
            if (prices[i] - min > profit)
                profit = prices[i] - min;
            if (prices[i] < min)
                min = prices[i];
        }

        return profit;

    }
}
