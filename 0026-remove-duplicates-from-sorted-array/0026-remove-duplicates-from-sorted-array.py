class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen=set()
        idx=0
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[idx]=nums[i]
                idx+=1
        return idx


        