class Solution(object):
    def numberOfBeams(self, bank):
        prev, ans = 0, 0
        for i in bank:
            c = i.count("1")
            if c == 0:
                continue
            else:
                ans += prev * c
                prev = c
        return ans