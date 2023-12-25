class Solution(object):
    def numDecodings(self, s):

        """
        :type s: str
        :rtype: int
        """

        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        if int(s[-1]) == 0:
            if int(s[-2]) not in [1, 2]:    #not 10, 20
                return 0
            else:                           #10, 20
                next1, next2 = 1, 0
        elif int(s[-2]) == 0:
            next1, next2 = 0, 1
        elif 10 < int(s[-2:]) < 27:
            next1, next2 = 2, 1
        else:
            next1, next2 = 1, 1
        i = len(s) - 3
        while i > -1:
            temp = 0
            if 9 < int(s[i:i+2]) < 27:
                temp = 1
            if int(s[i]) == 0:
                curr = 0
            else:
                curr = next1 + temp*next2
            next1, next2 = curr, next1
            i -= 1
        if len(s) == 2:
            return next1
        return curr
    