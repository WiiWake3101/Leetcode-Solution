from collections import Counter
from math import ceil

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        ans = 0
        for c in counter.values():
            if c == 1: 
                return -1
            ans += int(ceil(float(c) / 3))
        return ans
