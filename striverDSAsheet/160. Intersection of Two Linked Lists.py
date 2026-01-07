# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        visited = set()
        
        # Traverse list A and store nodes in the set
        curr = headA
        while curr:
            visited.add(curr)
            curr = curr.next
        
        # Traverse list B and check for intersection
        curr = headB
        while curr:
            if curr in visited:
                return curr
            curr = curr.next
        
        return None
