class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                x = stack.pop()
                y = stack.pop()

                if token == "+":
                    stack.append(y + x)
                elif token == "-":
                    stack.append(y - x)
                elif token == "*":
                    stack.append(y * x)
                else:
                    result = abs(y) // abs(x)

                    if (y < 0) != (x < 0):
                        result = -result

                    stack.append(result)

        return stack[-1]