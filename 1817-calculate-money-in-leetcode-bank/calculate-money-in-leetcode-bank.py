class Solution:
    def totalMoney(self, n: int) -> int:
        count = 0

        weeks = n//7+1

        for week in range(weeks):

            if week == weeks-1:
                for day in range(1,n%7+1):
                    count += week + day
            else:
                for day in range(1,8):
                    count += week + day

        return count
        