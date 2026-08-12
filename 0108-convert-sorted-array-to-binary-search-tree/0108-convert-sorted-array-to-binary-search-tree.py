# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
    
        def helper(left,right):
            if left>right:
                return None

            mid=(left+right)//2
            t=TreeNode(nums[mid])

            t.left=helper(left,mid-1)
            t.right=helper(mid+1,right)
            
            return t

        return helper(0,len(nums)-1)


        