# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()

        if head is None or head.next is None:
            return False

        curr = head
        while curr.next is not None:
            if id(curr.next) in s:
                return True
            s.add(id(curr.next))
            curr = curr.next

        return False
            