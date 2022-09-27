class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxRow = [max(row) for row in grid]
        maxCol = [max(col) for col in zip(*grid)]
        
        print(maxRow, maxCol)

        sum = 0
        for i in range(len(maxRow)):
            for j in range(len(maxCol)):
                sum += min(maxRow[i], maxCol[j]) - grid[i][j]
        
        return sum