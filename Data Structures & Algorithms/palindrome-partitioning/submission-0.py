class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        subset = []

        def backtracking(start):

            if start == len(s):
                result.append(subset.copy())
                return

            for end in range(start + 1, len(s) + 1):

                # current substring
                current = s[start:end]

                # check palindrome
                if current == current[::-1]:

                    subset.append(current)

                    # solve remaining string
                    backtracking(end)

                    # remove current choice
                    subset.pop()

        backtracking(0)

        return result