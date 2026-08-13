class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for i, h in enumerate(heights):

            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                width = i - index
                area = height * width

                max_area = max(max_area, area)

                start = index

            stack.append((start, h))

        for i, h in stack:
            width = len(heights) - i
            area = h * width

            max_area = max(max_area, area)

        return max_area