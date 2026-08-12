class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)

        if s[0] == '-':
            new_s = s[1:][::-1]
            final_s = '-' + new_s
            result = int(final_s)

            if result < -2**31 or result > 2**31 - 1:
                return 0

            return result

        new_s = s[::-1]
        result = int(new_s)

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result