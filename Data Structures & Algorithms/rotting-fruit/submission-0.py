class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row_len = len(grid)
        col_len = len(grid[0])

        # Store the minimum time at which each orange becomes rotten
        time = [[float("inf")] * col_len for _ in range(row_len)]

        def dfs(row, col, current_time):

            # Boundary check
            if row < 0 or row >= row_len or col < 0 or col >= col_len:
                return

            # Empty cell
            if grid[row][col] == 0:
                return

            # If we already reached this cell faster
            if current_time >= time[row][col]:
                return

            time[row][col] = current_time

            # Move in 4 directions
            dfs(row, col + 1, current_time + 1)
            dfs(row, col - 1, current_time + 1)
            dfs(row + 1, col, current_time + 1)
            dfs(row - 1, col, current_time + 1)

        # Start DFS from every rotten orange
        for row in range(row_len):
            for col in range(col_len):

                if grid[row][col] == 2:
                    dfs(row, col, 0)

        answer = 0

        # Check every fresh orange
        for row in range(row_len):
            for col in range(col_len):

                if grid[row][col] == 1:

                    # Never reached by a rotten orange
                    if time[row][col] == float("inf"):
                        return -1

                    answer = max(answer, time[row][col])

        return answer