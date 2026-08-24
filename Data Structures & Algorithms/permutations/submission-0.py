class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        used = set()

        def backtracking():
            if len(subset) == len(nums):
                result.append(subset.copy())
                return

            for i in range(len(nums)):
                if nums[i] in used:
                    continue

                subset.append(nums[i])
                used.add(nums[i])

                backtracking()

                subset.pop()
                used.remove(nums[i])

        backtracking()
        return result