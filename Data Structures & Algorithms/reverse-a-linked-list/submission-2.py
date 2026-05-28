# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr, next, next2 = head, None, None
        if curr is not None:
            next = curr.next
            curr.next = None

        while next is not None:
            next2 = next.next
            next.next = curr
            curr = next
            next = next2

        return curr

        
        
