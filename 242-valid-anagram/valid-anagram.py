class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n, m = len(s), len(t)
        if n != m:
            return False

        char_count = [0] * 26

        for char in s:
            char_count[ord(char) - ord('a')] += 1

        for char in t:
            if char_count[ord(char) - ord('a')] < 1:
                return False
            char_count[ord(char) - ord('a')] -= 1

        return True       