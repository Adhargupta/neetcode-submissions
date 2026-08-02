class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start<=end:
            n = (start + end) // 2

            if(nums[n]<target):
                start = n+1
            elif(nums[n]>target):
                end = n-1
            else:
                return n
        return -1