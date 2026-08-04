class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = []
        for i in range(len(temperatures)):
            found = False
            for j in range(i+1,len(temperatures)):
                if (temperatures[j]>temperatures[i]):
                    arr.append(j-i)
                    found = True
                    break
            if found==False:
                arr.append(0)
        return arr