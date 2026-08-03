import math
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:

            # Opening bracket
            if ch in "([{":
                stack.append(ch)

            # Closing bracket
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()

                if top != pairs[ch]:
                    return False

        return len(stack) == 0