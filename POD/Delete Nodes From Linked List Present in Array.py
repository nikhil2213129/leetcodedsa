class Solution(object):
    def modifiedList(self, nums, head):
        delete_set = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr and curr.next:
            if curr.next.val in delete_set:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
