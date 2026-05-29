# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = list()

        prev = head
        while prev is not None:
            s.append(prev)
            prev = prev.next
        
        l, r = 0, len(s) - 1
        while l < r:
            s[r].next = s[l].next
            s[l].next = s[r]
            l += 1
            r -= 1
        
        
        s[l].next = None
        


