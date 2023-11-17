class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        r=""
        for i in range (n) :
            if nums[i][i]=='0':
                r+='1'
            else:
                r+='0'
        return r