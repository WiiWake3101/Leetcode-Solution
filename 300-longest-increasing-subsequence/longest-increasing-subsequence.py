class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = [nums[0]]

        for i in nums:
            if ans[-1] < i:
                ans.append(i)
            else:
                seq= bisect.bisect_left(ans,i)
                ans[seq] = i

        return len(ans) 