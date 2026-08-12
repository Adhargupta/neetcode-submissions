class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        new_num = 0
        for i in nums:
            new_num ^= i
        return new_num