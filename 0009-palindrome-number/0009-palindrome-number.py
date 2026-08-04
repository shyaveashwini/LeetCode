class Solution(object):
    def isPalindrome(self, x):
        original=x
        rev=0
        while original>0:
            digit=original%10
            rev=rev*10+digit
            original=original//10
        if rev==x:
            return True
        else:
            return False
        