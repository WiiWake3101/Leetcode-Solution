class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = "13579"
        oddSet = set(odd)
        n = len(num)
        for i in range(n-1, -1, -1):
            if num[i] in oddSet:
                return num[:i+1]
        return ""