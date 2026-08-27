class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows_length = len(grid)
        cols_length = len(grid[0])
        count = 0
        def dfs(r,c):
            if r < 0 or r >= rows_length or c < 0 or c >= cols_length:
                return
            if grid[r][c] == "0":
                return
            grid[r][c] = '0'
            dfs(r,c-1)
            dfs(r,c+1)
            dfs(r+1,c)
            dfs(r-1,c)

        for i in range(rows_length):
            for j in range(cols_length):
                if grid[i][j] == '1':
                    count+=1
                    dfs(i,j)
        return count