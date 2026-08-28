class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        row_len = len(grid)
        col_len = len(grid[0])

        def dfs(row, col):

            if row < 0 or row >= row_len or col < 0 or col >= col_len:
                return 0

            if grid[row][col] == 0:
                return 0

            # visited
            grid[row][col] = 0

            area = 1

            area += dfs(row, col + 1)
            area += dfs(row, col - 1)
            area += dfs(row + 1, col)
            area += dfs(row - 1, col)

            return area

        max_area = 0

        for i in range(row_len):
            for j in range(col_len):

                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)

        return max_area