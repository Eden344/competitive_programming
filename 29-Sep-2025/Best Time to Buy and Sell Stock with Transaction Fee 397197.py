# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, not_buy = -prices[0],0
        for price in prices[1:]:
            buy, not_buy = max(buy,not_buy - price),max(not_buy,buy + price - fee)
        return not_buy