class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        ans = 0
        MOD = 10 ** 9 + 7
        for num in nums:
            rev = 0
            temp = num
            while temp:
                rev = rev * 10 + temp % 10
                temp //= 10
            num -= rev
            ans = (ans + dic[num]) % MOD
            dic[num] += 1
        return ans