class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            # Get the last bit of n
            bit = n & 1

            # Shift result left and add that bit
            result = (result << 1) | bit

            # Move to the next bit of n
            n >>= 1

        return result