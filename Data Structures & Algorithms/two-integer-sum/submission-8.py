class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            required = target - nums[i]
            if required in freq:
                arr = [i,freq[required]]
                arr.sort()
                return arr
            freq[nums[i]] = i

        return []
