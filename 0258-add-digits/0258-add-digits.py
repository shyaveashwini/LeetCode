class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        while num >= 10:  
            digit_sum = 0

            while num > 0:
                digit = num % 10
                digit_sum += digit
                num = num // 10

            num = digit_sum

        return num