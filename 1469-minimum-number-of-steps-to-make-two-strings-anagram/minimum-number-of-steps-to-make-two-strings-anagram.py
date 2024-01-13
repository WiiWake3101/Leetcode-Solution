class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        res = 0
        s_set = set(s)

        for char in s_set:
            diff = s.count(char) - t.count(char)
            if diff > 0:
                res += diff
        return res