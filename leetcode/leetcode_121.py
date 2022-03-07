# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# leetcode 121 : Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices) -> int:
        buy, sell, profit = 10001, -1, 0
        for price in prices:
            if price < buy:
                buy = price
            if price > sell:
                sell = price
                if sell - buy > profit:
                    profit = sell - buy
            print(price, profit)
        if profit <= 0:
            return 0
        else:
            return profit


prices = [7, 1, 5, 3, 6, 4]
Solution.maxProfit(0, prices)
