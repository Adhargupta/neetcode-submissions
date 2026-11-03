class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            speed = (left + right) // 2
            count = 0

            for i in piles:
                count += (i + speed - 1) // speed

            if count <= h:
                right = speed
            else:
                left = speed + 1

        return left