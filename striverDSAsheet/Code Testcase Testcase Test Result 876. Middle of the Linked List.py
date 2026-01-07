# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # first find the length of linked list
        # then divide length by 2
        # then traverse again to list if the relative length = 0
        # return the curr value
        length = 0
        curr = head
        while curr is not None:
            curr = curr.next
            length = length + 1
        rlength = 0
        curr = head
        while curr is not None:
            if rlength == length//2:
                return curr
            else:
                curr = curr.next
                rlength += 1
        return curr
