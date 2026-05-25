class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0
        if len(prices) == 2:
            return max(prices[1] - prices[0], 0)

        max_profit = 0

        p1, p2 = 0, 1
        while p2 < len(prices):
            if prices[p1] > prices[p2]:
                p1 = p2
                p2 += 1
                continue
            
            # 判斷今日盈虧
            max_profit = max(max_profit, prices[p2] - prices[p1])
            p2 += 1
            
        return max_profit
        


