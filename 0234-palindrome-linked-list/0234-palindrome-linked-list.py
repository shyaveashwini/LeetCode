# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        current = head

        list1 = []

        while current:
            list1.append(current.val)
            current = current.next

        if list1 == list1[::-1]:
            return True
        else:
            return False

        