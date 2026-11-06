class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        start = prices[0]
        for i in range(len(prices)):
            if prices[i] <= start:
                start = prices[i]
            else:
                diff = prices[i] - start
                maxi = max(maxi,diff)
        return maxi
