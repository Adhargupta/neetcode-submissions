class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0)+1

        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])

        for key, value in freq.items():
            bucket[value].append(key)

        arr = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                arr.append(num)
        return arr[:k]
