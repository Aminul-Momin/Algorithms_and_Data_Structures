


"""
LeetCode Problem # 980. Unique Paths III
TakenFrom: https://leetcode.com/problems/unique-paths-iii/

On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the 
ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:

1 <= grid.length * grid[0].length <= 20
"""


class UniquePath:
    
    def uniquePathsIII(self, grid):
        R, C = len(grid), len(grid[0])

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
                    yield nr, nc

        todo = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != -1:
                    todo += 1
                if val == 1:
                    sr, sc = r, c
                if val == 2:
                    tr, tc = r, c

        self.ans = 0

        def dfs(r, c, todo):
            todo -= 1
            if todo < 0:
                return
            if r == tr and c == tc:
                if todo == 0:
                    self.ans += 1
                return

            grid[r][c] = -1
            for nr, nc in neighbors(r, c):
                dfs(nr, nc, todo)
            grid[r][c] = 0

        dfs(sr, sc, todo)
        return self.ans

# TakenFrom: https://leetcode.com/problems/unique-paths-ii/solution/


def uniquePathsWithObstacles(self, M):
    """
    :type M: List[List[int]]
    :rtype: int
    """

    m = len(M)
    n = len(M[0])

    # If the starting cell has an obstacle, then simply return as there would be
    # no paths to the destination.
    if M[0][0] == 1:
        return 0

    # Number of ways of reaching the starting cell = 1.
    M[0][0] = 1

    # Filling the values for the first column
    for i in range(1, m):
        M[i][0] = int(M[i][0] == 0 and M[i-1][0] == 1)

    # Filling the values for the first row
    for j in range(1, n):
        M[0][j] = int(M[0][j] == 0 and M[0][j-1] == 1)

    # Starting from cell(1,1) fill up the values
    # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
    # i.e. From above and left.
    for i in range(1, m):
        for j in range(1, n):
            if M[i][j] == 0:
                M[i][j] = M[i-1][j] + M[i][j-1]
            else:
                M[i][j] = 0

    # Return value stored in rightmost bottommost cell. That is the destination.
    return M[m-1][n-1]



if __name__ == "__main__":
    up = UniquePath()
