class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        a,b = sorted(set(word1)),sorted(set(word2))
        if a != b:
            return False
        count1,count2 = [],[]
        for s1 in a:
            count1.append(word1.count(s1))
        for s2 in b:
            count2.append(word2.count(s2))
        if sorted(count1) == sorted(count2):
            return True