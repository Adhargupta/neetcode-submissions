class Solution:
    def maxArea(self, heights: List[int]) -> int:
        y = set()
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                pair = (heights[i],heights[j])
                height_pillar = min(pair)
                bridth_pillar = j-i
                area = height_pillar*bridth_pillar
                y.add(area)
        return max(y)