from collections import Counter
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        keys = sorted(count.keys(), reverse=True)
        ans = 0
        for i in range(1, len(keys)):
            count[keys[i]] += count[keys[i-1]]
            ans += count[keys[i-1]]
        return ans