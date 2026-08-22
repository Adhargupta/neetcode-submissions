class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(level):
            if level == len(nums):
                result.append(subset.copy())
                return 
            # exclude
            backtrack(level+1)
            # include
            subset.append(nums[level])
            backtrack(level+1)

            # backtrack
            subset.pop()

        backtrack(0)
        return result
