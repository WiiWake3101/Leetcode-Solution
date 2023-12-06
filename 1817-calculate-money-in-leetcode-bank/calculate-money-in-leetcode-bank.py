class Solution:
    def totalMoney(self, n: int) -> int:
        week, rest = divmod(n, 7)
        return 28 * week + week * (week - 1) * 7 // 2 + week * rest + (1+rest) * rest // 2

        