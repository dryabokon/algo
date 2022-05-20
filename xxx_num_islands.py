# https://leetcode.com/problems/number-of-islands/
# ----------------------------------------------------------------------------------------------------------------------
def numIslands(grid):

    def dfs(grid, i, j):

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]): return
        if grid[i][j]!= '1':return

        grid[i][j] = 'x'
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j - 1)

    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                count += 1
                dfs(grid, r, c)

    return count

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    res = numIslands(A)
    print(res)