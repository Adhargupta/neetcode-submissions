class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = []
        if(len(prices)-1==0):
            return 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                arr.append(prices[j]-prices[i])
        if max(arr)>0:
            return max(arr)
        else:
            return 0