class Solution:
    def largestDivisibleSubsetMemoization(self, nums: List[int]) -> List[int]:
        nums.sort()

        @cache
        def dfs(i, prev_index):
            if i == len(nums):
                return 0, -1

            length1, ele1 = dfs(i+1, prev_index)
            length2, ele2 = -1, -1

            if nums[i] % (nums[prev_index] if prev_index != -1 else 1) == 0:
                length2, ele2 = dfs(i+1, i)
                length2 += 1
            
            if length2 > length1:
                ladder_map[nums[i]] = ele2
                return length2, nums[i]
            else:
                return length1, ele1

        _, starting_ele = dfs(0, -1)
        res = []
        while starting_ele != -1:
            res.append(starting_ele)
            starting_ele = ladder_map[starting_ele]
        
        return res
    
    def largestDivisibleSubset(self, nums):
        subsets = {-1: set()}
        
        for num in sorted(nums):
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}
        
        return list(max(subsets.values(), key=len))