class Solution:
    def numberOfWays(self, corridor: str) -> int:
        cntseat = 0
        mod = 1000000007

        for ch in corridor:
            if ch == 'S':
                cntseat += 1

        if cntseat % 2 or cntseat == 0:
            return 0

        # Do not put any divider
        if cntseat == 2:
            return 1

        cnt = 0
        last = 0
        res = 1

        for i in range(len(corridor)):
            if corridor[i] == 'S':
                cnt += 1
                if cnt % 2 == 0:
                    last = i
                if cnt % 2 != 0 and cnt != 1:
                    res *= (i - last)
                    res %= mod

        return res
        