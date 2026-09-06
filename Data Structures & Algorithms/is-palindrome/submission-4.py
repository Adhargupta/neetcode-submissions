from math import floor
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.replace(' ','').lower()
        for i in t:
            if(i.isalnum()==False):
                t=t.replace(i,'')
        for i in range(floor(len(t)/2)):
            if(t[i]!=t[len(t)-i-1]):
                return False
        return True