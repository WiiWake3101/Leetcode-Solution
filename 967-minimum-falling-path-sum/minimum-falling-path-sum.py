class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1,m):
            for j in range(n):
                if j+1 < m and j > 0:
                    matrix[i][j] = matrix[i][j]+ min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])
                elif j == 0 :
                    matrix[i][j] = matrix[i][j]+ min(matrix[i-1][j], matrix[i-1][j+1])
                else :
                    matrix[i][j] = matrix[i][j]+ min(matrix[i-1][j-1], matrix[i-1][j])
        return min(matrix[m-1])
        