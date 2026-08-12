class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            s = bin(i)
            arr.append(s.count('1'))
        return arr