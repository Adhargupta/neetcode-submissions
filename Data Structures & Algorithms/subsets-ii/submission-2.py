class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        seen = set()

        def backtracking(level):
            if level == len(nums):
                key = tuple(sorted(subset))

                if key not in seen:
                    seen.add(key)
                    result.append(subset.copy())

                return

            # Exclude
            backtracking(level + 1)

            # Include
            subset.append(nums[level])
            backtracking(level + 1)
            subset.pop()

        backtracking(0)
        return result