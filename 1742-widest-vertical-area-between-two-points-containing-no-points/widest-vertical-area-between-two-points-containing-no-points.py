class Solution(object):
    def maxWidthOfVerticalArea(self, nums):
        ans = [i[0] for i in nums]
        maxi = 0
        ans.sort()
        for i in range(len(ans)-1):
            if ans[i + 1] - ans[i] > maxi:
                maxi = ans[i + 1] - ans[i]
        return maxi
        