class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit =0
        ref_price=float('inf')
        for price in prices:
            ref_price = min(ref_price,price)
            profit = price-ref_price
            max_profit = max(max_profit,profit)
        print(max_profit)
        return max_profit
