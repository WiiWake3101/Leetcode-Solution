class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = 0
        right_sum = sum(nums)

        answer = []
        for i in range(n):
            right_sum -= nums[i]
            answer.append((i * nums[i] - left_sum) + (right_sum - (n - i - 1) * nums[i]))
            left_sum += nums[i]

        return answer