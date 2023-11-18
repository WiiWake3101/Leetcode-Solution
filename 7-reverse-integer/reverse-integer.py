class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            a=int(str(x)[::-1])
        if x<=0:
            a= -1 * (int(str(x*-1)[::-1]))
        minimum=-2**31
        maximum=2**31-1
        if a not in range(minimum,maximum):
            return 0
        else:
            return a