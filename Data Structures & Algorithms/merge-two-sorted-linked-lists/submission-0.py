# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        head, curr = None, None
        while True:
            node = None
            if list1 is None and list2 is None:
                break
            elif list1 is None:
                node = list2
                list2 = list2.next
            elif list2 is None:
                node = list1
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    node = list1
                    list1 = list1.next
                else:
                    node = list2
                    list2 = list2.next
            if head is None:
                head = node
                curr = node
            else:
                curr.next = node
                curr = node
        return head
