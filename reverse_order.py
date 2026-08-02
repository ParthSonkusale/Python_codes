class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0

        sing = -1 if x < 0 else 1

        x = abs(x) # make integer positive

        while x != 0:
            digit = x % 10
            num = num * 10 + digit
            x = x // 10

        num *= sing 

        if num < -2**31 or num > 2**31 - 1:
            return 0

        return num