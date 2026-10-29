class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in range(len(strs)):
            n = len(strs[i])
            s += f'{n}#{strs[i]}'

        return s

    def decode(self, s: str) -> List[str]:
        arr=[]
        i=0
        while i < len(s):
            length = 0
            while s[i]!='#':
                length = length * 10 + int(s[i])
                i+=1

            i += 1
            arr.append(s[i:i + length])
            i += length
                
        return arr