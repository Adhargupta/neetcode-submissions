class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            length = len(i)
            t = str(length)
            s = s+t+"#"+i
        return s
    def decode(self, s: str) -> List[str]:
        arr = []

        while len(s) > 0:
            # Find the delimiter
            pos = s.find("#")

            # Get the length
            length = int(s[:pos])

            # Extract the string
            word = s[pos + 1 : pos + 1 + length]
            arr.append(word)

            # Remove the processed part
            s = s[pos + 1 + length :]
        return arr

