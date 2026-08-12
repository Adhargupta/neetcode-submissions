class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        temp = 0
        while True:
            a = n % 10
            temp += a ** 2

            if n // 10 > 0:
                n //= 10
            else:
                n = temp

                if n == 1:
                    return True

                if n in seen:
                    return False

                seen.add(n)
                temp = 0