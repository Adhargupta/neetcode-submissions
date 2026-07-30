class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj={}
        arr = []
        for i in nums:
            if i not in obj.keys():
                value = nums.count(i)
                obj[i]=value
                obj = dict(sorted(obj.items(), key=lambda x: x[1], reverse=True))
                for j in range(k):
                    arr = list(obj.keys())[:k]
        return arr