class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        price_buy = prices[0]

        for price in prices[1:]:
            if price_buy > price:
                price_buy = price
            
            profit = max(profit, price - price_buy)

        return profit
