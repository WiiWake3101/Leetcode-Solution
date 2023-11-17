class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        n=len(arr)
        flag=1
        for i in range (flag,n):
            if arr[i]>=flag+1:
                flag+=1
        return flag