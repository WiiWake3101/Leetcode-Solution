class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        x, y = 1, 2
        if n == 1: return x
        if n == 2: return y
        for n in range(3, n + 1):
            x, y = y, x + y
        return y
        
        