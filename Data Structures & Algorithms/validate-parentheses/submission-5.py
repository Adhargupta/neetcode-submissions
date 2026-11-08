class Solution:
    def isValid(self, s: str) -> bool:
        obj = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        stack = []

        for i in s:
            if i not in obj:
                if not stack:
                    return False
                if i != obj[stack[-1]]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False