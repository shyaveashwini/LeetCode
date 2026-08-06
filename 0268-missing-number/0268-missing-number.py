class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet=list(range(len(nums)+1))
        for num in nums:
            numSet.remove(num)
        return numSet[0]