class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        candidates.sort()

        def backtracking(start, current_sum):
            if current_sum == target:
                result.append(subset.copy())
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if current_sum + candidates[i] > target:
                    break

                subset.append(candidates[i])
                backtracking(i + 1, current_sum + candidates[i])
                subset.pop()

        backtracking(0, 0)

        return result