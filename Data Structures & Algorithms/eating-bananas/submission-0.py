import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Smallest possible eating speed
        left = 1

        # Largest possible eating speed
        right = max(piles)

        answer = right

        while left <= right:

            # Guess an eating speed
            k = (left + right) // 2

            hours = 0

            # Calculate total hours needed at speed k
            for pile in piles:
                hours += math.ceil(pile / k)

            # If Koko can finish within h hours
            if hours <= h:
                answer = k          # This speed works
                right = k - 1       # Try a smaller speed

            else:
                left = k + 1        # Too slow, increase speed

        return answer