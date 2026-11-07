class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = {}
        maxi = 1
        start = 0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i],0)+1
            t=max(freq.values())
            replaced = i-start+1-t
            if replaced > k:
                freq[s[start]] -= 1
                start+=1
            maxi = max(maxi,i-start+1)

        return maxi