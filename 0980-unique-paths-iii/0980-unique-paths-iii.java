class Solution {
    private int totalPaths = 0;

    public int uniquePathsIII(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        int startR = 0, startC = 0;
        int emptyCount = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    startR = i;
                    startC = j;
                } else if (grid[i][j] == 0) {
                    emptyCount++;
                }
            }
        }

        dfs(grid, startR, startC, emptyCount + 1);

        return totalPaths;
    }

    private void dfs(int[][] grid, int r, int c, int remaining) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] == -1) {
            return;
        }

        if (grid[r][c] == 2) {
            if (remaining == 0) {
                totalPaths++;
            }
            return;
        }

        int temp = grid[r][c];
        grid[r][c] = -1;

        dfs(grid, r + 1, c, remaining - 1);
        dfs(grid, r - 1, c, remaining - 1);
        dfs(grid, r, c + 1, remaining - 1);
        dfs(grid, r, c - 1, remaining - 1);

        grid[r][c] = temp;
    }
}