class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(level):
            # Target reached
            if sum(subset) == target:
                result.append(subset.copy())
                return

            # Sum exceeded
            if sum(subset) > target:
                return

            # No more numbers
            if level == len(nums):
                return

            # Exclude current number
            backtrack(level + 1)

            # Include current number
            subset.append(nums[level])
            backtrack(level)

            # Undo
            subset.pop()

        backtrack(0)
        return result
