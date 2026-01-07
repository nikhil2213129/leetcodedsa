# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k==0:
            return head

        # checking list length
        l=1
        t=head
        while(t.next):
            t=t.next
            l+=1
        
        #checking k value wrto l
        k%=l
        if(k==0):return head

        # connecting end to start
        t.next=head
        # Traversing

        nt=head
        for _ in range(l-k-1):
            nt=nt.next
        
        #disconnecting
        newhead=nt.next
        nt.next=None

        return newhead
