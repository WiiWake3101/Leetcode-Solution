class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        def bit_msk(s):
            return sum(1 << (ord(c) - 97) for c in s)

        def len_msk(msk):
            return bin(msk).count('1')

        def fn(k, current_msk, arr, memo = {}):
            tpl = (current_msk, arr)
            if tpl in memo:
                return memo[tpl]
            current_max = 0
            for i in range(k, len(arr)):
                if not arr[i] & current_msk:
                    next_msk = current_msk + arr[i]
                    current_max = max(current_max, len_msk(next_msk), fn(i+1, next_msk, arr))
            memo[tpl] = current_max
            return current_max
        s = ''.join(arr)
        if len(set(s)) == len(s):
            return len(s)
        return fn(0, 0, tuple(bit_msk(a) for a in arr if len(a) == len(set(a))))