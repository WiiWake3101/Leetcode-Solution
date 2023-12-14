class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        ans = [''.join(w for w in word1)]
        ans2 = [''.join(w for w in word2)]
        return ans == ans2