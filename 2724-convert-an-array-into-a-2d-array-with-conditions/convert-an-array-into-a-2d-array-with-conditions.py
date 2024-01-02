class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        freq = [0] * (len(nums) + 1)
        
        ans = []
        for c in nums:
            if freq[c] >= len(ans):
                ans.append([])
# Store the integer in the list corresponding to its current frequency.
            ans[freq[c]].append(c)
            freq[c] += 1
        
        return ans