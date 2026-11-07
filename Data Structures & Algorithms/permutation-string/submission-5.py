class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}

        for i in range(len(s1)):
            freq[s1[i]] = freq.get(s1[i],0)+1

        freq2 = {}
        start = 0
        for i in range(len(s2)):
            freq2[s2[i]] = freq2.get(s2[i],0)+1

            if i-start+1 > len(s1):
                freq2[s2[start]] -= 1
                if freq2[s2[start]] == 0:
                    del freq2[s2[start]]
                start+=1
            if freq2 == freq:
                return True
        return False
