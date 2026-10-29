class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 0
        max_count = 0
        freq=set()
        for i in range(len(nums)):
            freq.add(nums[i])

        freq = sorted(freq)

        for i in range(len(freq)-1):

            if freq[i+1] - freq[i] != 1:
                max_count = max(max_count,count)
                count = 0
            else:
                count+=1
        max_count = max(max_count, count) 

        return max_count+1