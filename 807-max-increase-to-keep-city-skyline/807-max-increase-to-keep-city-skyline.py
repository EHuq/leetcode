class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]
        
        sum = 0
        for i in range(len(row_maxes)):
            for j in range(len(col_maxes)):
                sum += min(row_maxes[i], col_maxes[j]) - grid[i][j]
        
        return sum