class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new = []
        temp = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(j!=i):
                    temp = temp*nums[j]
            new.append(temp)
            temp=1
        return new