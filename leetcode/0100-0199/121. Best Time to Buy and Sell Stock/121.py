class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minP = prices[0]
        
        for i in prices[1:]:
            maxP = max(maxP, i - minP)
            minP = min(minP, i)

        return maxP
