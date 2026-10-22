class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}

        for i in s:
            freq1[i] = freq1.get(i,0) + 1
        for i in t:
            freq2[i] = freq2.get(i,0) + 1
        return freq1 == freq2