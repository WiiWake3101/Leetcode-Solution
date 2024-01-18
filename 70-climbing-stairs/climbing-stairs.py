class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        prv1 = 1
        prv2 = 2
        x = 0
        for i in range(2,n):
            x = prv1 + prv2
            prv1 = prv2
            prv2 = x
        return x
        