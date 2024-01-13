class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        count = [0]*26
        # Storing the difference of frequencies of characters in t and s.
        for i in range(len(s)):
            count[ord(t[i]) - ord('a')] += 1
            count[ord(s[i]) - ord('a')] -= 1

        ans = 0
        # Adding the difference where string t has more instances than s.
        # Ignoring where t has fewer instances as they are redundant and
        # can be covered by the first case.
        for i in range(26):
            ans += max(0, count[i])
        
        return ans