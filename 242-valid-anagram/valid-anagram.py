class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        tem = set(s)
        for i in tem:
            if not (i in t and i in s and s.count(i) == t.count(i)):
                return False
        return True   