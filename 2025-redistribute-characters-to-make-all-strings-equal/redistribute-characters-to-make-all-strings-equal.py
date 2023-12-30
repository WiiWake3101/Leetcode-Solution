class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        total_len = 0
        for word in words:
            total_len += len(word)
        if total_len % len(words) != 0:
            return False
        occ = {}
        for word in words:
            for ch in word:
                if ch in occ:
                    occ[ch] +=1 
                else:
                    occ[ch] = 1
        for counts in occ.values():
            if counts % len(words) != 0:
                return False
        return True
        