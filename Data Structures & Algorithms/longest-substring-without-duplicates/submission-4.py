class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        start = 0
        maxi = 0

        for i in range(len(s)):

            while s[i] in seen:
                seen.remove(s[start])
                start += 1

            seen.add(s[i])
            maxi = max(maxi, i - start + 1)

        return maxi
            
